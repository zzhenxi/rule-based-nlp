'''
Q. Extract bijective phrases 

1. Statistics 

NUM_LINES 
NUM_SRC_TOKENS
NUM_TGT_TOKENS
MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT
MULTIPLE_TRANSLATIONS_IN_TGT_TO_SRC
NUM_TOKENS_EQUAL_IN_LINE
NUM_TOKENS_INEQUAL_IN_LINE

2. Details

MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT Valentine
MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT ('밸런타인', 3, 확률, (4797, 'Bobby Valentine', '바비 밸런타인'))
MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT ('발렌타인', 1, 확률, (9662, 'Dori Valentine', '도리 발렌타인'))
MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT ('발렌틴', 1, 확률, (22104, 'Karen Valentine', '카렌 발렌틴'))


MULTIPLE_TRANSLATIONS_IN_TGT_TO_SRC 솔
MULTIPLE_TRANSLATIONS_IN_TGT_TO_SRC ('Soul', 1, 확률, (8810, 'David Soul', '데이비드 솔'))
MULTIPLE_TRANSLATIONS_IN_TGT_TO_SRC ('Sol', 2, 확률, (40956, 'Sol Bamba', '솔 밤바'))
MULTIPLE_TRANSLATIONS_IN_TGT_TO_SRC ('Saul', 2, 확률 (39096, 'Saul Perlmutter', '솔 펄머터'))
'''

def extract_bijective_phrases(FILE_PATH, cat):
    statistics = {'NUM_LINES':0, 
                  'NUM_SRC_TOKENS':0, 
                  'NUM_TGT_TOKENS':0, 
                  'MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT':0, 
                  'MULTIPLE_TRANSLATIONS_IN_TGT_TO_SRC':0,
                    'NUM_TOKENS_EQUAL_IN_LINE':0, 
                  'NUM_TOKENS_INEQUAL_IN_LINE':0}
    
    src2tgt = {}
    tgt2src = {}
    with open(FILE_PATH) as fo:
        for ln, line in enumerate(fo, 1):
            src, tgt = line[:-1].split('\t')
            src_list = src.lower().split()
            tgt_list = tgt.lower().split()
            statistics['NUM_LINES'] += 1
            statistics['NUM_SRC_TOKENS'] += len(src_list)
            statistics['NUM_TGT_TOKENS'] += len(tgt_list)
            
            if len(src_list) == len(tgt_list):
                statistics['NUM_TOKENS_EQUAL_IN_LINE'] += 1
                
                for s, t in zip(src_list, tgt_list):
                    if s not in src2tgt:
                        src2tgt[s] = [0, {}]
                    src2tgt[s][0] += 1
                    if t not in src2tgt[s][1]:
                        src2tgt[s][1][t] = []
                    src2tgt[s][1][t].append((ln, src, tgt))
                
                for t, s in zip(src_list, tgt_list):
                    if s not in src2tgt:
                        src2tgt[s] = [0, {}]
                    src2tgt[s][0] += 1
                    if t not in src2tgt[s][1]:
                        src2tgt[s][1][t] = []
                    src2tgt[s][1][t].append((ln, src, tgt))           
            else:
                statistics['NUM_TOKENS_INEQUAL_IN_LINE'] += 1
                
    if cat == 'MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT':
        for k, v in src2tgt.items():
            total_num = v[0]
            print(cat, k)
            for _k, _v in v[1].items():
                p = round(len(_v)/total_num, 3)
                print(cat, (_k, len(_v), p, _v[0]))
            print()
    elif cat == 'MULTIPLE_TRANSLATIONS_IN_TGT_TO_SRC':
        for k, v in tgt2src.items():
            total_num = v[0]
            print(cat, k)
            for _k, _v in v[1].items():
                p = round(len(_v)/total_num, 3)
                print(cat, (_k, len(_v), p, _v[0]))
            print()

extract_bijective_phrases('06.enko.dict.person', 'MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT')

'''
[result]
MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT 프라부파다
MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT ('prabhupada', 1, 1.0, (6, 'A. C. Bhaktivedanta Swami Prabhupada', 'A. C. 박티베단타 스와미 프라부파다'))

MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT edward
MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT ('에드워드', 61, 0.953, (7, 'A. Edward Sutherland', 'A. 에드워드 서덜랜드'))
MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT ('에두아르트', 1, 0.016, (6147, 'Charles Edward', '카를 에두아르트'))
MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT ('에도아르도', 1, 0.016, (10178, 'Edward', '에도아르도'))
MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT ('에드바르트', 1, 0.016, (10193, 'Edward Dembowski', '에드바르트 뎀보프스키'))

MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT sutherland
MULTIPLE_TRANSLATIONS_IN_SRC_TO_TGT ('서덜랜드', 3, 1.0, (7, 'A. Edward Sutherland', 'A. 에드워드 서덜랜드'))
'''