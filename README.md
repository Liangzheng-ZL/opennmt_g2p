# OpenNMT-based Seq2Seq-G2P(grapheme-to-phoneme) model.
In this report, we try to find an efficient way to do the conversion of grapheme to phoneme, epecially on person names. We used the latest cmudict-0.7b\[1] as the dataset of our G2P model. We divided the datset into train set and test set. The conversion of grapheme-to-phoneme is similar with transduction. As a classic neural machine translation model and eural sequence learning, OpenNMT works well on sequence modeling and transduction problems. We tested whether OpenNMT can be used for seq2seq-g2p. Our results showed that OpenNMT-based G2P model can generate promising pronunciation, and the words in test set were completelya different from the words in train set, proving that OpenNMT is suitable for Seq2Seq-G2P.


