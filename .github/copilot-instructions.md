# One's Brothers News Bot
One's Brothers is a satirical Portuguese news bot that scrapes Brazilian news sites (G1, UOL, BBC Brasil), creates humorous summaries with progressively hostile tone based on usage frequency, and generates audio using either gTTS (free) or ElevenLabs API (premium voices).

**ALWAYS reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.**

## Working Effectively

### Bootstrap and Dependencies
- Python 3.12+ application - **NEVER CANCEL** any build/install commands
- Install system dependencies first:
  ```bash
  sudo apt update && sudo apt install -y python3-requests python3-bs4 python3-dotenv python3-feedparser python3-gtts mpg123 ffmpeg
  ```
  Takes 3-5 minutes. Set timeout to 10+ minutes.

- **CRITICAL**: pip install often fails due to network timeouts. Use system packages when possible:
  ```bash
  # If pip fails with timeout errors, use apt packages:
  sudo apt install -y python3-requests python3-bs4 python3-dotenv python3-feedparser python3-gtts
  ```

- Setup script (./setup.sh) - takes 20-30 seconds, but **pip dependencies often fail** due to network issues:
  ```bash
  time ./setup.sh  # Creates venv and attempts pip install
  ```
  **Expected**: PyGObject installation fails due to network timeouts. This is normal - the tray app won't work but core functionality will.

### Configuration
- Copy environment file: `cp .env.example .env`
- **Optional** API configuration in .env:
  - `ELEVENLABS_API_KEY` - for premium voices (optional)
  - `OPENAI_API_KEY` - for AI-powered summaries (optional)
  - App works in FREE mode without any API keys using gTTS and simple summaries

### Core Application Testing
- **WITHOUT network access** (sandboxed environments):
  ```bash
  # Create mock dependencies for offline testing
  python3 -c "
  import sys
  # Mock schedule module
  class MockSchedule:
      def every(self): return self
      def day(self): return self
      def at(self, t): return self
      def do(self, f): return self
      def run_pending(self): pass
  sys.modules['schedule'] = MockSchedule()
  
  # Mock openai module  
  class MockOpenAI:
      def __init__(self, **kwargs): pass
  sys.modules['openai'] = MockOpenAI()
  
  # Test import
  from news_reporter_bot import NewsReporterBot
  print('✅ Core imports successful')
  "
  ```

- **WITH network access**:
  ```bash
  # Test news scraping (requires internet)
  python3 news_scraper.py  # Takes 5-10 seconds
  
  # Test full application
  python3 news_now.py  # Takes 30-60 seconds - NEVER CANCEL
  ```

## Validation Scenarios
- **ALWAYS test core imports** with mock dependencies when network is restricted
- **Core functionality test**: Run `python3 -c "from news_reporter_bot import NewsReporterBot; bot = NewsReporterBot(); bot.test_components()"` 
- **Free mode validation**: Without API keys, app should use gTTS and simple summaries
- **Premium mode validation**: With API keys, app should use ElevenLabs voices and OpenAI summaries
- **Audio generation test**: Check that audio files are created in news_output/ directory
- **Network failure graceful handling**: App should handle failed news scraping and network timeouts

## Critical Timing and Cancellation Rules
- **NEVER CANCEL**: pip install commands - they timeout frequently but may succeed on retry
- **NEVER CANCEL**: Setup script (./setup.sh) - takes 20-30 seconds normally, up to 5 minutes if network is slow
- **NEVER CANCEL**: News scraping - takes 5-15 seconds per site, up to 60 seconds total timeout
- **NEVER CANCEL**: Voice generation - gTTS takes 2-5 seconds, ElevenLabs takes 10-20 seconds
- **Expected timeouts**: Set 10+ minute timeouts for installation commands, 2+ minutes for execution commands

## Installation and Runtime Dependencies

### System Requirements
- Python 3.12+ (verified working version)
- Internet access for news scraping and voice generation (gTTS/ElevenLabs)
- Audio playback: mpg123, ffmpeg, or vlc for audio playback

### Network Dependency Limitations
- **News scraping**: Requires access to g1.globo.com, uol.com.br, bbc.com
- **gTTS voice generation**: Requires access to translate.google.com  
- **ElevenLabs**: Requires API access to elevenlabs.io
- **OpenAI**: Requires API access to openai.com
- **pip install**: Requires access to pypi.org (frequently times out)

### Fallback Behavior
- No network: Core imports work with mocked dependencies
- No APIs: Uses free gTTS and simple summaries
- No audio players: Audio files still generated but not played

## Key Projects and Entry Points

### Main Scripts
- `news_reporter_bot.py` - Main orchestrator with interactive menu
- `news_now.py` - Quick execution script (no menu)
- `news_tray.py` - System tray application (requires GUI)
- `setup.sh` - Installation script

### Core Components  
- `news_scraper.py` - Scrapes G1, UOL, BBC Brasil
- `news_summarizer.py` - Creates humorous summaries (uses OpenAI if available)
- `voice_generator.py` - Audio generation (ElevenLabs or gTTS fallback)
- `news_cache.py` - Tracks usage for progressive hostility
- `config.py` - Multi-language and voice configuration

### Test Scripts
- `test_voices.py` - Test different voice options
- `test_callum.py` - Test specific ElevenLabs voice
- `test_*.py` - Various API and functionality tests

## Common Tasks and File Structure

### Repository Root Contents
```
├── README.md, README_PTBR.md     # Documentation  
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment template
├── setup.sh, news_launcher.sh    # Setup and launch scripts
├── config.py                     # Multi-language configuration
├── news_*.py                     # Core application modules
├── test_*.py                     # Test scripts
├── NewsReporter.desktop          # Desktop integration files
└── news_output/                  # Generated audio and script files
```

### Output Files
- `news_output/` directory contains:
  - `news_YYYYMMDD_HHMMSS.json` - Raw scraped news
  - `script_YYYYMMDD_HHMMSS.txt` - Generated text script  
  - `news_YYYYMMDD_HHMMSS.mp3` - Generated audio file

### Voice Options
**Free (gTTS)**: Portuguese, Spanish, English, French, Italian
**Premium (ElevenLabs)**: callum, charlie, roger, liam, eric, jessica, giovanni, george

## Debugging Common Issues

### Network/Installation Issues
- **pip timeouts**: Use apt packages instead: `sudo apt install python3-requests python3-bs4`
- **No news scraped**: Check internet access to Brazilian news sites
- **gTTS fails**: Requires access to translate.google.com
- **"No module named 'schedule'"**: Install manually or use mocked version for testing

### Audio Issues  
- **No audio playback**: Install `mpg123` or `ffmpeg`: `sudo apt install -y mpg123 ffmpeg`
- **Audio file empty**: Check network access for gTTS or ElevenLabs API key
- **"Cannot play audio"**: Multiple fallback players attempted, install additional: `sudo apt install vlc sox`

### API Configuration
- **ElevenLabs not working**: Check API key in .env file, module import errors indicate missing elevenlabs package
- **OpenAI summaries fail**: App falls back to simple summaries automatically
- **Voice generation fails**: App attempts ElevenLabs first, then falls back to gTTS

## Testing Commands Summary
```bash
# Quick validation (always works)
python3 -c "import requests, bs4; print('✅ Core deps available')"

# Full setup test (may timeout)
time ./setup.sh  # 20-30 seconds normal, 5+ minutes if slow network

# Component test with mocks (always works)
python3 -c "
import sys
class Mock: pass
sys.modules['schedule'] = Mock()
sys.modules['openai'] = Mock()
from news_reporter_bot import NewsReporterBot
print('✅ Imports successful')
"

# Full application test (requires network)
python3 news_now.py  # 30-60 seconds - NEVER CANCEL
```

**CRITICAL REMINDER**: This application requires internet access for full functionality. In sandboxed environments, use mocked dependencies for code validation and testing.