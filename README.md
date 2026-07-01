# F.I.L.E.

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![Platform](https://img.shields.io/badge/platform-windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A lightweight, Python-based desktop utility designed to automatically sort, declutter, and organize disorganized storage directories based purely on file extensions.  
It works only on file locations — not file contents.

## Features

- **Automated Routing:** Maps miscellaneous downloads straight to categorized structural folders.
- **Dynamic Path Mapping:** Relocates files using absolute paths to prevent any operational target mismatches.
- **Retro Interface:** Built with a clean, classic flat layout mimicking native desktop designs.
- **Basic System Safety:** Operates strictly locally using standard system environments without requiring registry changes or admin rights.
- **Zero Dependencies:** Built entirely with native libraries, requiring no external package installations.

## How to Use

1. Navigate to the Releases panel on the right sidebar of this page.
2. Download the standalone production asset: `FILE_Setup.exe` (or the portable edition).
3. Launch the operational workspace interface, use **Browse...** to select your target folder (e.g., Downloads), and click **Organize Folder**.

## Behavior Summary

![image](/assets/user_interface.png)

| Category        | Destination Folder Name | Managed Extensions                                                                                      |
| :-------------- | :---------------------- | :------------------------------------------------------------------------------------------------------ |
| **Media**       | Videos, Audio, Images   | `.mp4`, `.mkv`, `.avi`, `.mov`, `.flv`, `.mp3`, `.wav`, `.aac`, `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp` |
| **Data & Docs** | PDFs, Documents, Excel  | `.pdf`, `.docx`, `.doc`, `.txt`, `.rtf`, `.xlsx`, `.xls`, `.csv`                                        |
| **Compressed**  | Archives                | `.zip`, `.rar`, `.7z`                                                                                   |

## Tech Stack

- **Language:** Python
- **GUI:** Tkinter (Classic layout style)
- **Packaging:** PyInstaller

## Output Example

| Input             | Output Path             |
| :---------------- | :---------------------- |
| `tutorial.mp4`    | `Videos/tutorial.mp4`   |
| `invoice.pdf`     | `PDFs/invoice.pdf`      |
| `data_sheet.xlsx` | `Excel/data_sheet.xlsx` |

## Notes

- No recursive folder scanning (only selected directory root level is processed).
- Existing subfolders are skipped to avoid infinite processing loops.
- File extensions are read uniformly regardless of upper/lowercase formatting.
- File integrity remains completely intact; assets are only moved, never modified.
