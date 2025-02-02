# PressLinkFormatting
The code in this repository helps parsing specially structured text into wordpress code. This reduces the manual work, which needs to be done to move the given data to a wordpress page.

The data processed by the given script shall have the following form:
(YYYY/MM/DD) Caption
URL1
URL2
URL...
URL N

It is possible thate the data to parse only specifies a single or N URLs.

For example the data could be:
```
(2025/01/10) Heading
https://newspaper1.com/article1
https://newspaper2.org/article1
```

By the given script the previous specified data will be transformed to:
```
<!-- wp:paragraph -->
<p>(2025/01/10) Heading<br><a href="https://newspaper1.com/article1">https://newspaper1.com/article1</a><br><a href="https://newspaper2.org/article1">https://newspaper2.org/article1</a></p>
<!-- /wp:paragraph -->
```

This means that a single block of the input data will be converted to a wordpress paragraph, where the data and the heading, will get an own row. The links which are listed below the heading will be be extracted to seperate html anchor elements for every single URL.

Addtionally to the primary input data a header can be specified, which will be added prior the converted data.

## How to run the script
The script has the following parameters which have to be called in a **predefined order**:
1. The path to the file with the input data
2. The path to the file where the output will be stored
3. (optional) The path to the file with the header data, if some content shall be prepend to the converted data.

The script can be called like this:
```
python3 press-link-formatter-objectoriented.py [path_to_input_file] [path_to_output_file] [(optional)path_to_header_file]
```
