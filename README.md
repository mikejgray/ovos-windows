# ovos-windows

Running OpenVoiceOS (OVOS) natively on Windows. No containers, no VMs, no WSL, no Cygwin, no nothing. Just Windows and Python!

This is very much a proof-of-concept installation. If you are not comfortable with both Python and Powershell, and you're looking for a single .exe to run, this isn't the repository for you. Hopefully, this will be a good starting point for someone to create a more user-friendly installer.

## Prerequisites

- VLC installed
- Python 3.8 or later
- Poetry installed (for package management)
- [cmdmp3 installed (for audio playback)](https://github.com/jimlawless/cmdmp3?tab=readme-ov-file)
- `mkdir $HOME\.cache\json_database`
- `mkdir $HOME\.config\mycroft`
- `cp mycroft.conf.example $HOME\.config\mycroft\mycroft.conf`
- `mkdir $env:APPDATA\..\Local\Temp\skills`
- `mkdir $env:APPDATA\..\Local\Temp\skills\ovos-skill-alerts.openvoiceos`

## Installation

- Install Python
- Install Poetry
- `poetry install`
- `poetry shell`
- `.\ovos.ps1`

## Hacks

- `code $profile` to edit your PowerShell profile, then add this function to make a fake `aplay` command:

```powershell
function aplay {$PlayWav=New-Object System.Media.SoundPlayer
    $PlayWav.SoundLocation=$args[0]
    $PlayWav.playsync()
}
```

Unnecessary if you have VLC or cmdmp3, and also doesn't work with OVOS because Python doesn't load your PowerShell profile, but kind of fun!

## Known Issues

- Numerous OVOS skills are _not Windows-friendly_ and will need to be modified to work on Windows, including several default skills. Most skill developers don't run Windows and don't test on Windows, so you'll need to do some debugging and testing to get them to work. This is a great way to contribute back to the community!
- Padacioso is a slow intent engine, but will work on Windows. Padatious is faster, but must be compiled from source, and it's non-trivial to do so. If you get good instructions please PR back to this repository.
- Audio response is quite slow because Windows doesn't have great native support for command-line audio.
