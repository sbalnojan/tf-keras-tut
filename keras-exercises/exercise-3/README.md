# Exericse 3 - All about Embeddings

a) The dummy model: Build a one layer .Sequential() model with one embedding
for 1001 inputs and 100 outputs. We feed one by one (input=length=1).

b) Add some layer to map your 100 outputs to one numerical value. Then
use the data from generate_dummy_data() (numbers 1,....,1000 with labels
1,1,...,2,...,100) and take a look at the predictions before and after
fitting, also take a look at the embedding layer values itself (yes,
you can access the values of individual layers... see the solution or figure out 
yourself).

c) GloVe: 
https://nlp.stanford.edu/projects/glove/


d) Word2Vec: Next task is to preload a specific pretrained embedding,
Word2Vec into an Embedding layer. 
https://code.google.com/archive/p/word2vec/


More) There's more, but we won't dive into eLMo and BERT for now.