import pandas as pd
from src import common


def taxonomy_analysis(df,
                      all_intcols,
                      sample1_colnames,
                      sample2_colnames,
                      test,
                      threshold,
                      paired):

    # determine which taxonomic ranks are in user-provided dataset
    user_tax = set(basic_tax).intersection(set(df))

    # add up through ranks
    norm_intensity_all_ranks = pd.concat([rel_abundance_rank(df, x, all_intcols) for x in user_tax])

    # test
    if test:
        results = common.test_norm_intensity(norm_intensity_all_ranks, sample1_colnames, sample2_colnames, threshold, paired)
    else:
        results = norm_intensity_all_ranks

    return results


tax = ["superkingdom",
       "kingdom",
       "subkingdom",
       "superphylum",
       "phylum",
       "subphylum",
       "superclass",
       "class",
       "subclass"
       "infraclass",
       "superorder",
       "order",
       "suborder",
       "infraorder",
       "parvorder",
       "superfamily",
       "family",
       "subfamily",
       "tribe",
       "subtribe",
       "genus",
       "subgenus",
       "species_group",
       "species_subgroup",
       "species",
       "subspecies",
       "varietas",
       "forma"]

basic_tax = ["phylum",
             "class",
             "order",
             "family",
             "genus",
             "species"]

def rel_abundance_rank(df, rank, all_intcols):
    summed_abund = df.groupby(by=rank)[all_intcols].sum(axis=0)
    # normalize to each sample
    rel_abundance = summed_abund / summed_abund.sum(axis=0)
    rel_abundance['rank'] = rank
    return rel_abundance