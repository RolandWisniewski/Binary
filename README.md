# Binary Encoder and Decoder

This Python script demonstrates how to encode text into binary format and store it in separate text files, then decode it back to its original form.

## 📖 Description
The script performs the following tasks:
1. Text Processing:
  - Takes a predefined text based on the **Zen of Python**.
  - Cleans up extra spaces and splits it into lines.
2. Binary Encoding:
  - Converts each character in the text to its binary ASCII representation.
  - Stores the encoded text in separate files (`plikX.txt`).
3. Binary Decoding:
  - Reads the binary data from the files.
  - Converts it back to the original text.
4. File Cleanup:
  - Deletes all the generated `.txt` files after decoding.

## 🔧 How to Run
1. Save the script as `binary_encoder.py`.
1. Run it in your Python environment:

```bash
python binary_encoder.py
```

## 📝 Output Example
The script outputs the original text after decoding:

```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
```

## 🛠️ Requirements
* Python 3.6 or higher
* No external libraries required.
 
## ⚠️ Notes
* Generated files (`plikX.txt`) are automatically deleted after decoding.
* Make sure you have write permissions in the directory where the script is run.

👤 Author
* [RolandWisniewski](https://github.com/RolandWisniewski)
