## VerbNet's WordNet-FrameNet Mappings

This is a script for extracting the WordNet-FrameNet Mappings from [VerbNet](https://github.com/cu-clear/verbnet).

### Download:
* `git clone --recurse-submodules https://github.com/nu11us/VerbNet-WN-FN-Mappings`

### Configuration:
* Create a virtual environment: `python -m venv venv`
* Enter virtual environment: `source venv/bin/activate`
* `pip install -r requirements.txt`
* In Python:
    * `import nltk`
    * `nltk.download('wordnet')`
    * `nltk.download('framenet_v17')`

### To Extract Mapping to CSV
* Default: `python mapper.py`
* To a given output: `python mapper.py <output>`
* To a given output with a custom VerbNet directory: `python mapper.py <output> <verbnet>`

### VerbNet Citation
Please cite the following:
* Karin Kipper, Anna Korhonen, Neville Ryant, Martha Palmer, A Large-scale Classification of English Verbs, Language Resources and Evaluation Journal, 42(1), pp. 21-40, Springer Netherland, 2008.
