import sys
#fr_tgt = open("cmudict.tgt",encoding = "ISO-8859-1")
fr_src = open("cmudict_clean.src")
fr_tgt = open("cmudict_clean.tgt")
fr_train_stc = open("train_s.txt","w",encoding = 'utf-8')
fr_train_tgt = open("train_t.txt","w",encoding = 'utf-8')
fr_valid_stc = open("valid_s.txt","w",encoding = 'utf-8')
fr_valid_tgt = open("valid_t.txt","w",encoding = 'utf-8')
# fr_test_stc = open("test_s.txt","w",encoding = 'utf-8')
# fr_test_tgt = open("test_t.txt","w",encoding = 'utf-8')

cnt = 0
for (line_s,line_t) in zip(fr_src.readlines(),fr_tgt.readlines()):

	if cnt % 100 == 0:
                fr_valid_stc.write(line_s)
                fr_valid_tgt.write(line_t)
                cnt = cnt+1
                continue
	fr_train_stc.write(line_s)
	fr_train_tgt.write(line_t)
	cnt = cnt + 1
