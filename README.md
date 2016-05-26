# huffman-tools

[Huffman](https://en.wikipedia.org/wiki/Huffman_coding) tools to compress &amp; decompress

Build in **Python 3**

## Todo:
- Compression
    - [x] Extract content from file
    - [x] Compress file
    - [ ] Read file in byte array
- Decompression
    - [x] Extract compressed content from file
    - [x] Decompress file
    - [x] Decompressed file content is the same as the original file content
    - [ ] Read file in byte array
- [x] CLI (Command Line Interface)

## Usage

```bash
[TP_HUFFMAN] $ python3 huffman.py -c leHorla.txt
# OUTPUT => Your content has compressed in: leHorlaEncode.txt
[TP_HUFFMAN] $ python3 huffman.py -d leHorlaEncode.txt
# OUTPUT => Your content is in: leHorlaDecode.txt
```
Hugo POULIQUEN
