# ClaudinMatcher
Takes fasta files containing Amino Acid Sequences of Claudin Proteins and filters for sequences with certain electrophysiological features.

Simple pattern matching on input-file, either .txt or .fasta to find only those gene sequences which have the expected features.
This pattern matcher anticipates the following dependance of amino acid chains and ion-channel-forming behaviour:
For strict coverage it expects a W close to the beginning and an R close to the end of the string, otherwise it doesn't.
For both levels an ion-channel-forming claudin is expected to have a G or S or N, followed by an I or L, followed by a W, then two random
aa's then a C and another C following within the next 20 positions.
The differentiation between kat-, and an-ion channels is as follows:
