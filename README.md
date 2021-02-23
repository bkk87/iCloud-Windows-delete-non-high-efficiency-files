# iCloud Windows Sync Client: Delete all non-high-efficiency files

When using the iCloud Windows Sync Client you have the option to also download 'high-efficiency' files. This means that the iCloud Client will not only download files in `JPG` and `MOV` format but will also additionally download these files in `HEIF` format. `HEIF` is great because it compresses better, but it is not as platform-compatible as `JPG`.

Unfortunately, there is no option in the iCloud Client to only download files in `HEIF` format.

This scrpt checks if the same file is available in `HEIF` format and will subsequentely delete the corresponding `JPG` or `MOV` file.

Please use the Windws 7/8 version of the iCloud Windows Tool. The newer Version do not allow you to download your complete photo library.