import torch
import torch.nn as nn


class DilatedAttentionBlockS(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()

        self.input_projection = nn.Conv2d(
            in_channels,
            in_channels,
            kernel_size=1,
        )

        self.dilated_conv_1 = nn.Sequential(
            nn.Conv2d(
                in_channels,
                in_channels,
                kernel_size=3,
                padding=1,
                dilation=1,
            ),
            nn.InstanceNorm2d(in_channels, affine=True),
            nn.LeakyReLU(),
        )

        self.dilated_conv_2 = nn.Sequential(
            nn.Conv2d(
                in_channels,
                in_channels,
                kernel_size=3,
                padding=2,
                dilation=2,
            ),
            nn.InstanceNorm2d(in_channels, affine=True),
            nn.LeakyReLU(),
        )

        self.dilated_conv_3 = nn.Sequential(
            nn.Conv2d(
                in_channels,
                in_channels,
                kernel_size=3,
                padding=3,
                dilation=3,
            ),
            nn.InstanceNorm2d(in_channels, affine=True),
            nn.LeakyReLU(),
        )

        self.average_pool = nn.AvgPool2d(
            kernel_size=3,
            stride=1,
            padding=1,
        )

        self.maximum_pool = nn.MaxPool2d(
            kernel_size=3,
            stride=1,
            padding=1,
        )

        self.attention_features = nn.Sequential(
            nn.Conv2d(
                6 * in_channels,
                in_channels,
                kernel_size=3,
                padding=1,
            ),
            nn.InstanceNorm2d(in_channels, affine=True),
            nn.LeakyReLU(),
        )

        self.attention_projection = nn.Conv2d(
            in_channels,
            in_channels,
            kernel_size=1,
        )

        self.channel_attention = nn.Softmax(dim=1)

        self.output_projection = nn.Sequential(
            nn.Conv2d(
                in_channels,
                out_channels,
                kernel_size=1,
            ),
            nn.InstanceNorm2d(out_channels, affine=True),
            nn.LeakyReLU(),
        )

    def forward(self, inputs):
        projected = self.input_projection(inputs)

        features_1 = self.dilated_conv_1(projected)
        features_2 = self.dilated_conv_2(features_1)
        features_3 = self.dilated_conv_3(features_2)

        multiscale_features = torch.cat(
            [features_1, features_2, features_3],
            dim=1,
        )

        pooled_features = torch.cat(
            [
                self.average_pool(multiscale_features),
                self.maximum_pool(multiscale_features),
            ],
            dim=1,
        )

        attention = self.attention_features(pooled_features)
        attention = self.attention_projection(attention)
        attention = self.channel_attention(attention)

        return self.output_projection(attention * inputs)


class DANetS(nn.Module):
    def __init__(self, num_classes=2, base_channels=8):
        super().__init__()

        channels = base_channels

        self.stem = nn.Sequential(
            nn.Conv2d(
                3,
                channels,
                kernel_size=3,
                padding=1,
            ),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )

        self.block_1 = DilatedAttentionBlockS(channels, channels)
        self.pool_1 = nn.MaxPool2d(kernel_size=2, stride=2)

        self.block_2 = DilatedAttentionBlockS(channels, 2 * channels)
        self.block_3 = DilatedAttentionBlockS(2 * channels, 2 * channels)
        self.pool_2 = nn.MaxPool2d(kernel_size=2, stride=2)

        self.block_4 = DilatedAttentionBlockS(2 * channels, 4 * channels)
        self.block_5 = DilatedAttentionBlockS(4 * channels, 4 * channels)
        self.pool_3 = nn.MaxPool2d(kernel_size=2, stride=2)

        self.block_6 = DilatedAttentionBlockS(4 * channels, 8 * channels)
        self.block_7 = DilatedAttentionBlockS(8 * channels, 8 * channels)
        self.pool_4 = nn.MaxPool2d(kernel_size=2, stride=2)

        self.block_8 = DilatedAttentionBlockS(8 * channels, 16 * channels)
        self.block_9 = DilatedAttentionBlockS(16 * channels, 16 * channels)

        self.global_pool = nn.AvgPool2d(kernel_size=7, stride=2)
        self.flatten = nn.Flatten()

        self.classifier = nn.Sequential(
            nn.Linear(16 * channels, 8 * channels),
            nn.ReLU(),
            nn.Linear(8 * channels, num_classes),
            nn.LogSoftmax(dim=1),
        )

    def forward(self, inputs):
        features = self.stem(inputs)

        features = self.block_1(features)
        features = self.pool_1(features)

        features = self.block_2(features)
        features = self.block_3(features)
        features = self.pool_2(features)

        features = self.block_4(features)
        features = self.block_5(features)
        features = self.pool_3(features)

        features = self.block_6(features)
        features = self.block_7(features)
        features = self.pool_4(features)

        features = self.block_8(features)
        features = self.block_9(features)

        features = self.global_pool(features)
        features = self.flatten(features)

        return self.classifier(features)
