# MKV to MP4 Converter

A Python script that converts MKV video files to MP4 format using FFmpeg with multi-threading support and a progress bar.

## Features
- Converts multiple MKV files to MP4 simultaneously using multi-threading
- Displays a progress bar showing conversion status
- Uses FFmpeg's stream copying for fast conversion without re-encoding
- Preserves original video and audio quality
- Creates output directory if it doesn't exist
- Thread-safe progress tracking

## Prerequisites

### Software Requirements
- Python 3.6+
- FFmpeg installed on your system

### Python Dependencies
- tqdm (for progress bar)

## Installation

1. Clone or download this repository
2. Install Python dependencies:
```bash
pip install tqdm