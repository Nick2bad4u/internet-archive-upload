# Internet Archive Upload Action

[![latest GitHub release.](https://flat.badgen.net/github/release/Nick2bad4u/internet-archive-upload?color=cyan)](https://github.com/Nick2bad4u/internet-archive-upload/releases) [![GitHub stars.](https://flat.badgen.net/github/stars/Nick2bad4u/internet-archive-upload?color=yellow)](https://github.com/Nick2bad4u/internet-archive-upload/stargazers) [![GitHub forks.](https://flat.badgen.net/github/forks/Nick2bad4u/internet-archive-upload?color=green)](https://github.com/Nick2bad4u/internet-archive-upload/forks) [![GitHub open issues.](https://flat.badgen.net/github/open-issues/Nick2bad4u/internet-archive-upload?color=red)](https://github.com/Nick2bad4u/internet-archive-upload/issues)

- This action was originally forked from [palewire/internet-archive-upload](https://github.com/palewire/internet-archive-upload).
- It allows you to upload files or directories to the Internet Archive (archive.org) and set metadata for the uploaded items.
- The action supports uploading single files, multiple files, or entire directories, and it can handle various metadata fields to describe the content being uploaded.

## Inputs: _(Required)_

- These 4 fields, **MUST** be present in your action configuration.
- *Missing any 1 of these will cause the upload to fail.*

| Input Name     | Description                                                                 |
| -------------- | --------------------------------------------------------------------------- |
| `access-key` | Your archive.org access key                                                 |
| `secret-key` | Your archive.org secret key                                                 |
| `identifier` | The unique identifier of the archive.org item where the file will be stored |
| `files`      | File or folder path(s) to upload. Supports a single path, a glob pattern, or a comma-separated list of paths |

## Additional Non-Metadata Optional Inputs

| Input Name | Description |
| --- | --- |
| `log-level` | Log verbosity level for the uploader. Allowed values: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`. Defaults to `INFO`. |

## Outputs

| Output Name | Description |
| --- | --- |
| `item-url` | Archive.org details page URL for the target identifier, e.g. `https://archive.org/details/<identifier>` |

### Supported Metadata Fields Inputs: _(Optional)_

- All of the following fields are optional.
- They are used to define additional metadata on your uploads according to the [Archive.org Metadata Schema](https://archive.org/developers/metadata-schema/index.html "Internet Archive Metadata Docs").
- *Please refer to the metadata docs above if you have any questions about uploading specific metadata.*

| Input Name                    | Description                                                                    | Example                                                                                                      |
| ----------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `adaptive_ocr`              | Allows deriver to skip a page that would otherwise disrupt OCR                 | true                                                                                                         |
| `aspect_ratio`              | Ratio of the pixel width and height of a video stream (e.g. 4:3, 16:9)         | 4:3                                                                                                          |
| `betterpdf`                 | Indicates that the derive module should create a higher quality PDF derivative | true                                                                                                         |
| `bookreader-defaults`       | Bookreader display mode (e.g. mode/1up, mode/2up, mode/thumb)                  | mode/1up                                                                                                     |
| `bwocr`                     | Allows deriver to OCR specific pages as B&W if color is causing failure        | 001                                                                                                          |
| `call_number`               | Contributing library's local call number                                       | 6675707, NC 285.1 P9287m                                                                                     |
| `ccnum`                     | Closed Captioning Number                                                       | cc5                                                                                                          |
| `closed_captioning`         | Indicates whether item contains closed captioning files (yes/no)               | yes                                                                                                          |
| `color`                     | Indicates whether media is in color or black and white (`color` or `black and white`) | color                                                                                                   |
| `condition`                 | Condition of media (e.g. Good, Fair, Poor)                                     | Good                                                                                                         |
| `condition-visual`          | Condition of artwork or printed materials                                      | Good                                                                                                         |
| `contributor`               | Comma-separated list of contributors                                           | Robarts - University of Toronto                                                                              |
| `coverage`                  | Comma-separated list of geographic or subject areas covered by item            | GB-LND                                                                                                       |
| `creator`                   | Comma-separated list of creators                                               | Austen, Jane, 1775-1817, Ralph Burns                                                                         |
| `creator-alt-script`        | Creator in alternate script                                                    | [alternate script]                                                                                           |
| `date`                      | Date of publication (YYYY, YYYY-MM, or YYYY-MM-DD)                             | 1965, 2013-05-25, [n.d.]                                                                                     |
| `description`               | Describes the media stored in the item                                         | Cinemascope homage to the city of San Francisco made by amateur filmmaker and inventor Tullio Pellegrini.    |
| `external-identifier`       | Comma-separated list of URLs or identifiers to outside resources               | urn:publisher_catalog_id:88697 03614 2                                                                       |
| `fixed-ppi`                 | To change the ppi to a specific resolution                                     | 300                                                                                                          |
| `isbn`                      | Comma-separated list of ISBN-10 or ISBN-13                                     | 3540212507, 031294716X                                                                                       |
| `issn`                      | Comma-separated list of ISSN identifiers                                       | 2528-7788, 1943-345X                                                                                         |
| `lccn`                      | Comma-separated list of Library of Congress Call Numbers                       | 2004045278                                                                                                   |
| `language`                  | Comma-separated list of languages                                              | eng, Italian, None                                                                                           |
| `licenseurl`                | URL of the copyright license                                                   | [http://creativecommons.org/licenses/by-nd/3.0/](http://creativecommons.org/licenses/by-nd/3.0/)                |
| `notes`                     | Additional notes about the item                                                | [any string]                                                                                                 |
| `oclc-id`                   | Comma-separated list of OCLC identifiers                                       | 37432884                                                                                                     |
| `openlibrary`               | Deprecated. Open Library edition identifier                                    | OL2769393M                                                                                                   |
| `openlibrary_author`        | Comma-separated list of Open Library authors                                   | OL52922A                                                                                                     |
| `openlibrary_edition`       | Open Library edition identifier                                                | OL2769393M                                                                                                   |
| `openlibrary_subject`       | Comma-separated list of Open Library subjects                                  | openlibrary_staff_picks                                                                                      |
| `openlibrary_work`          | Open Library work identifier                                                   | OL675783W                                                                                                    |
| `page-progression`          | Determines direction pages will be "turned" in a book (lr/rl)                  | lr                                                                                                           |
| `possible-copyright-status` | Information relevant to copyright status                                       | The Centers for Medicare & Medicaid Services Library is unaware of any copyright restrictions for this item. |
| `ppi`                       | Pixels per inch                                                                | 300                                                                                                          |
| `publisher`                 | Publisher of the media                                                         | New York : R.R. Bowker Co.                                                                                   |
| `related-external-id`       | Comma-separated list of related external identifiers                           | urn:isbn:0671038303                                                                                          |
| `rights`                    | Rights statement                                                               | Permission is granted under the Wikimedia Foundation's ...                                                   |
| `scandate`                  | Date and time the media was captured                                           | 20170329201345                                                                                               |
| `scanner`                   | Machinery used to digitize or collect the media                                | scribe2.nj.archive.org                                                                                       |
| `size`                      | Size of physical item digitized                                                | 10.0                                                                                                         |
| `sound`                     | Indicates whether media has sound or is silent (`sound` or `silent`)           | sound                                                                                                        |
| `source`                    | Source of media                                                                | folio, Comcast Cable, CD                                                                                     |
| `sponsor`                   | The person or organization that funded the digitization or collection          | Kahle-Austin Foundation                                                                                      |
| `subject`                   | Comma-separated list of subjects/topics for the item                           | France                                                                                                       |
| `title`                     | The human-readable title for the item                                          | San Francisco (1955 Cinemascope film)                                                                        |
| `title-alt-script`          | Title in alternate script                                                      | [alternate script]                                                                                           |
| `volume`                    | Volume number or name                                                          | 15                                                                                                           |
| `year`                      | Year of publication (deprecated, use date)                                     | 1996                                                                                                         |

## Usage Examples

> [!TIP]
> For supply-chain security, pin this action to a full commit SHA instead of a mutable tag such as `latest`.
> The latest SHA for this repo is:
> ```
> 1cdb640f1bd8b06c29ef86a7d323d8c2e51eda89
> ```
> Use it as: `nick2bad4u/internet-archive-upload@1cdb640f1bd8b06c29ef86a7d323d8c2e51eda89`

> [!NOTE]
> Set `log-level: DEBUG` in action inputs for verbose troubleshooting output (or override via `IA_LOG_LEVEL`).

> [!IMPORTANT]
> Best practice for this action is to rely on the step exit code for success/failure. It intentionally does not expose status/message outputs, because those are redundant with normal GitHub Actions failure handling and are less reliable when a step fails fast.

> [!NOTE]
> The action does expose one useful output: `item-url`, which is the expected Internet Archive details URL derived from the target identifier.

### Upload a single file with metadata

```yaml
name: Upload a file to archive.org with metadata
jobs:

  job:
    name: Upload a file
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v6

      - name: Upload file to archive.org
        id: ia_upload
        uses: nick2bad4u/internet-archive-upload@1cdb640f1bd8b06c29ef86a7d323d8c2e51eda89
        with:
            # Required fields
            access-key: ${{ secrets.IA_ACCESS_KEY }}
            secret-key: ${{ secrets.IA_SECRET_KEY }}
            identifier: your-item
            files: your-file.jpg

            # Optional metadata fields
            title: "My Archive Title"
            creator: "Jane Doe,John Smith"
            subject: "example,archive,upload"
            date: "2025-05-29"
            language: "English"
            betterpdf: true

      - name: Print uploaded item URL
        run: echo "Item URL: ${{ steps.ia_upload.outputs.item-url }}"
```

### Upload a directory of files

```yaml
name: Upload a directory of files to archive.org with metadata
jobs:

  job:
    name: Upload directory
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v6

      - name: Upload directory to archive.org
        uses: nick2bad4u/internet-archive-upload@1cdb640f1bd8b06c29ef86a7d323d8c2e51eda89
        with:
          # Required fields
          access-key: ${{ secrets.IA_ACCESS_KEY }}
          secret-key: ${{ secrets.IA_SECRET_KEY }}
          identifier: your-item
          files: your-files/

          # Optional metadata fields
          title: "My Archive Title"
          creator: "Jane Doe,John Smith"
          subject: "example,archive,upload"
          date: "2025-05-29"
          language: "English"
          betterpdf: true
```

### Example of a real-world usage in a GitHub Actions workflow

- Action is located here in the repo here: [`.github/workflows/internet-archive-upload.yml`](https://github.com/Nick2bad4u/internet-archive-upload/blob/main/.github/workflows/internet-archive-upload.yml "Uploader File Location")
- Check workflow run logs here: [Upload Releases to Archive.org - Logs](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/internet-archive-upload.yml "Log FIles")

```yaml
name: Upload Releases to Archive.org

on:
  workflow_dispatch:
  push:

concurrency:
  group: IA-${{ github.ref }}
  cancel-in-progress: true

jobs:
  upload-windows:
    runs-on: ubuntu-latest
    steps:

      - name: Download release tarball + zip
        id: download_zip
        uses: robinraju/release-downloader@daf26c55d821e836577a15f77d86ddc078948b05 # v1.12
        with:
          repository: Nick2bad4u/internet-archive-upload
          latest: true
          tarBall: true
          zipBall: true
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Upload tarball + zip to archive.org
        uses: Nick2bad4u/internet-archive-upload@1cdb640f1bd8b06c29ef86a7d323d8c2e51eda89 # main
        with:
          access-key: ${{ secrets.IA_ACCESS_KEY }}
          secret-key: ${{ secrets.IA_SECRET_KEY }}
          identifier: Github-Action-IA-Archiver-${{ steps.download_zip.outputs.tag_name }}
          files: ./
        continue-on-error: true
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

```

## Issues

If you encounter any issues or have feature requests, please open an issue in the [GitHub repository](https://github.com/nick2bad4u/internet-archive-upload/issues "Open Issues").

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Nick2bad4u/internet-archive-upload/blob/main/LICENSE "License File") file for details.

## Contributing

If you want to contribute to this project, please fork the repository and submit a pull request. Contributions are welcome!

## Acknowledgements

This action was originally created by [**Ben Welsh**](https://github.com/palewire/internet-archive-upload "PaleWire Internet Archive Uploader Repo"). It has been forked and maintained by [Nick2bad4u](https://github.com/nick2bad4u/internet-archive-upload "Nick2bad4u's Profile").
