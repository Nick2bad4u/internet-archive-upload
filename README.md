## Inputs

* `access-key`: Your archive.org access key
* `secret-key`:  Your archive.org secret key
* `identifier`: The unique identifier of the archive.org item where the file will be stored
* `files`: The file or folder path inside the action's filesystem to upload

### Supported Metadata Fields Inputs

* `adaptive_ocr`: Allows deriver to skip a page that would otherwise disrupt OCR
* `aspect_ratio`: Ratio of the pixel width and height of a video stream (e.g. 4:3, 16:9)
* `betterpdf`: Indicates that the derive module should create a higher quality PDF derivative
* `bookreader-defaults`: Bookreader display mode (e.g. mode/1up, mode/2up, mode/thumb)
* `bwocr`: Allows deriver to OCR specific pages as B&W if color is causing failure
* `call_number`: Contributing library’s local call number
* `ccnum`: Closed Captioning Number
* `closed_captioning`: Indicates whether item contains closed captioning files (yes/no)
* `color`: Indicates whether media is in color or black and white
* `condition`: Condition of media (e.g. Good, Fair, Poor)
* `condition-visual`: Condition of artwork or printed materials
* `contributor`: Comma-separated list of contributors
* `coverage`: Comma-separated list of geographic or subject areas covered by item
* `creator`: Comma-separated list of creators
* `creator-alt-script`: Creator in alternate script
* `date`: Date of publication (YYYY, YYYY-MM, or YYYY-MM-DD)
* `description`: Describes the media stored in the item
* `external-identifier`: Comma-separated list of URLs or identifiers to outside resources
* `fixed-ppi`: To change the ppi to a specific resolution
* `isbn`: Comma-separated list of ISBN-10 or ISBN-13
* `issn`: Comma-separated list of ISSN identifiers
* `lccn`: Comma-separated list of Library of Congress Call Numbers
* `language`: Comma-separated list of languages
* `licenseurl`: URL of the copyright license
* `notes`: Additional notes about the item
* `oclc-id`: Comma-separated list of OCLC identifiers
* `openlibrary`: Deprecated. Open Library edition identifier
* `openlibrary_author`: Comma-separated list of Open Library authors
* `openlibrary_edition`: Open Library edition identifier
* `openlibrary_subject`: Comma-separated list of Open Library subjects
* `openlibrary_work`: Open Library work identifier
* `page-progression`: Determines direction pages will be “turned” in a book (lr/rl)
* `possible-copyright-status`: Information relevant to copyright status
* `ppi`: Pixels per inch
* `publisher`: Publisher of the media
* `related-external-id`: Comma-separated list of related external identifiers
* `rights`: Rights statement
* `scandate`: Date and time the media was captured
* `scanner`: Machinery used to digitize or collect the media
* `size`: Size of physical item digitized
* `sound`: Indicates whether media has sound or is silent
* `source`: Source of media
* `sponsor`: The person or organization that funded the digitization or collection
* `subject`: Comma-separated list of subjects/topics for the item
* `title`: The human-readable title for the item
* `title-alt-script`: Title in alternate script
* `volume`: Volume number or name
* `year`: Year of publication (deprecated, use date)

## Usage

Upload a single file with metadata:

```yaml
name: Example action
jobs:
  job:
    name: Upload
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Upload file to archive.org
        uses: palewire/internet-archive-upload@v1
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
            betterpdf: "true"
```

Upload a directory of files:

```yaml
name: Example action
jobs:
  job:
    name: Upload
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Upload file to archive.org
        uses: palewire/internet-archive-upload@v1
        with:
          access-key: ${{ secrets.IA_ACCESS_KEY }}
          secret-key: ${{ secrets.IA_SECRET_KEY }}
          identifier: your-item
          files: your-files/
          title: "My Archive Title"
```
