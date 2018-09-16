import unittest

import metaquant.SampleGroups
from metaquant.util import io
import os
from metaquant.util.utils import DATA_DIR


class TestIO(unittest.TestCase):

    def testTaxonomyIn(self):
        taxin = os.path.join(DATA_DIR, 'test', 'unipept_a_thaliana_result_w_pep.tab')
        df = io.read_taxonomy_table(taxin, 'peptide', 'lca', )
        # the first peptide is assigned to 'root'
        self.assertEqual(df['lca'][0], 'root')

    def testFunctionIn(self):
        funcin = os.path.join(DATA_DIR, 'test', 'multiple_func.tab')
        df = io.read_function_table(funcin, 'peptide', func_colname='go')
        self.assertEqual(df['go']['A'], 'GO:0008152')

    def testMerge(self):
        taxin = os.path.join(DATA_DIR, 'test', 'tax_join.tab')
        funcin = os.path.join(DATA_DIR, 'test', 'func_join.tab')
        int_in = os.path.join(DATA_DIR, 'test', 'int_join.tab')
        sinfo = '{"1":["int1", "int2"]}'
        samp_grps = metaquant.SampleGroups.SampleGroups(sinfo)
        dfs_joined = io.read_and_join_files('taxfn', pep_colname='peptide',
                                            int_file=int_in, samp_groups=samp_grps,
                                            tax_file=taxin, func_file=funcin, tax_colname='lca',
                                            func_colname='go')

        self.assertSetEqual(set(dfs_joined), {'int1', 'int2', 'lca', 'go'})


if __name__=='__main__':
    unittest.main()
