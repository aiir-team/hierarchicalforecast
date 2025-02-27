# Autogenerated by nbdev

d = { 'settings': { 'branch': 'main',
                'doc_baseurl': '/hierarchicalforecast/',
                'doc_host': 'https://Nixtla.github.io',
                'git_url': 'https://github.com/Nixtla/hierarchicalforecast/',
                'lib_path': 'hierarchicalforecast'},
  'syms': { 'hierarchicalforecast.core': { 'hierarchicalforecast.core.HierarchicalReconciliation': ( 'core.html#hierarchicalreconciliation',
                                                                                                     'hierarchicalforecast/core.py'),
                                           'hierarchicalforecast.core.HierarchicalReconciliation.__init__': ( 'core.html#hierarchicalreconciliation.__init__',
                                                                                                              'hierarchicalforecast/core.py'),
                                           'hierarchicalforecast.core.HierarchicalReconciliation._prepare_fit': ( 'core.html#hierarchicalreconciliation._prepare_fit',
                                                                                                                  'hierarchicalforecast/core.py'),
                                           'hierarchicalforecast.core.HierarchicalReconciliation.bootstrap_reconcile': ( 'core.html#hierarchicalreconciliation.bootstrap_reconcile',
                                                                                                                         'hierarchicalforecast/core.py'),
                                           'hierarchicalforecast.core.HierarchicalReconciliation.reconcile': ( 'core.html#hierarchicalreconciliation.reconcile',
                                                                                                               'hierarchicalforecast/core.py'),
                                           'hierarchicalforecast.core._build_fn_name': ( 'core.html#_build_fn_name',
                                                                                         'hierarchicalforecast/core.py'),
                                           'hierarchicalforecast.core._reverse_engineer_sigmah': ( 'core.html#_reverse_engineer_sigmah',
                                                                                                   'hierarchicalforecast/core.py')},
            'hierarchicalforecast.evaluation': { 'hierarchicalforecast.evaluation.HierarchicalEvaluation': ( 'evaluation.html#hierarchicalevaluation',
                                                                                                             'hierarchicalforecast/evaluation.py'),
                                                 'hierarchicalforecast.evaluation.HierarchicalEvaluation.__init__': ( 'evaluation.html#hierarchicalevaluation.__init__',
                                                                                                                      'hierarchicalforecast/evaluation.py'),
                                                 'hierarchicalforecast.evaluation.HierarchicalEvaluation.evaluate': ( 'evaluation.html#hierarchicalevaluation.evaluate',
                                                                                                                      'hierarchicalforecast/evaluation.py'),
                                                 'hierarchicalforecast.evaluation._metric_protections': ( 'evaluation.html#_metric_protections',
                                                                                                          'hierarchicalforecast/evaluation.py'),
                                                 'hierarchicalforecast.evaluation.energy_score': ( 'evaluation.html#energy_score',
                                                                                                   'hierarchicalforecast/evaluation.py'),
                                                 'hierarchicalforecast.evaluation.log_score': ( 'evaluation.html#log_score',
                                                                                                'hierarchicalforecast/evaluation.py'),
                                                 'hierarchicalforecast.evaluation.mqloss': ( 'evaluation.html#mqloss',
                                                                                             'hierarchicalforecast/evaluation.py'),
                                                 'hierarchicalforecast.evaluation.mse': ( 'evaluation.html#mse',
                                                                                          'hierarchicalforecast/evaluation.py'),
                                                 'hierarchicalforecast.evaluation.msse': ( 'evaluation.html#msse',
                                                                                           'hierarchicalforecast/evaluation.py'),
                                                 'hierarchicalforecast.evaluation.scaled_crps': ( 'evaluation.html#scaled_crps',
                                                                                                  'hierarchicalforecast/evaluation.py')},
            'hierarchicalforecast.methods': { 'hierarchicalforecast.methods.BottomUp': ( 'methods.html#bottomup',
                                                                                         'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.BottomUp._get_PW_matrices': ( 'methods.html#bottomup._get_pw_matrices',
                                                                                                          'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.BottomUp.fit': ( 'methods.html#bottomup.fit',
                                                                                             'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.BottomUp.fit_predict': ( 'methods.html#bottomup.fit_predict',
                                                                                                     'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.ERM': ('methods.html#erm', 'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.ERM.__init__': ( 'methods.html#erm.__init__',
                                                                                             'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.ERM._get_PW_matrices': ( 'methods.html#erm._get_pw_matrices',
                                                                                                     'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.ERM.fit': ( 'methods.html#erm.fit',
                                                                                        'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.ERM.fit_predict': ( 'methods.html#erm.fit_predict',
                                                                                                'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.HReconciler': ( 'methods.html#hreconciler',
                                                                                            'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.HReconciler._get_sampler': ( 'methods.html#hreconciler._get_sampler',
                                                                                                         'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.HReconciler._reconcile': ( 'methods.html#hreconciler._reconcile',
                                                                                                       'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.HReconciler.predict': ( 'methods.html#hreconciler.predict',
                                                                                                    'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.HReconciler.sample': ( 'methods.html#hreconciler.sample',
                                                                                                   'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.MiddleOut': ( 'methods.html#middleout',
                                                                                          'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.MiddleOut.__init__': ( 'methods.html#middleout.__init__',
                                                                                                   'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.MiddleOut._get_PW_matrices': ( 'methods.html#middleout._get_pw_matrices',
                                                                                                           'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.MiddleOut.fit': ( 'methods.html#middleout.fit',
                                                                                              'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.MiddleOut.fit_predict': ( 'methods.html#middleout.fit_predict',
                                                                                                      'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.MiddleOut.predict': ( 'methods.html#middleout.predict',
                                                                                                  'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.MinTrace': ( 'methods.html#mintrace',
                                                                                         'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.MinTrace.__init__': ( 'methods.html#mintrace.__init__',
                                                                                                  'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.MinTrace._get_PW_matrices': ( 'methods.html#mintrace._get_pw_matrices',
                                                                                                          'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.MinTrace.fit': ( 'methods.html#mintrace.fit',
                                                                                             'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.MinTrace.fit_predict': ( 'methods.html#mintrace.fit_predict',
                                                                                                     'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.OptimalCombination': ( 'methods.html#optimalcombination',
                                                                                                   'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.OptimalCombination.__init__': ( 'methods.html#optimalcombination.__init__',
                                                                                                            'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.TopDown': ( 'methods.html#topdown',
                                                                                        'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.TopDown.__init__': ( 'methods.html#topdown.__init__',
                                                                                                 'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.TopDown._get_PW_matrices': ( 'methods.html#topdown._get_pw_matrices',
                                                                                                         'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.TopDown.fit': ( 'methods.html#topdown.fit',
                                                                                            'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.TopDown.fit_predict': ( 'methods.html#topdown.fit_predict',
                                                                                                    'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods._get_child_nodes': ( 'methods.html#_get_child_nodes',
                                                                                                 'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods._reconcile_fcst_proportions': ( 'methods.html#_reconcile_fcst_proportions',
                                                                                                            'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.crossprod': ( 'methods.html#crossprod',
                                                                                          'hierarchicalforecast/methods.py'),
                                              'hierarchicalforecast.methods.lasso': ( 'methods.html#lasso',
                                                                                      'hierarchicalforecast/methods.py')},
            'hierarchicalforecast.probabilistic_methods': { 'hierarchicalforecast.probabilistic_methods.Bootstrap': ( 'probabilistic_methods.html#bootstrap',
                                                                                                                      'hierarchicalforecast/probabilistic_methods.py'),
                                                            'hierarchicalforecast.probabilistic_methods.Bootstrap.__init__': ( 'probabilistic_methods.html#bootstrap.__init__',
                                                                                                                               'hierarchicalforecast/probabilistic_methods.py'),
                                                            'hierarchicalforecast.probabilistic_methods.Bootstrap.get_prediction_levels': ( 'probabilistic_methods.html#bootstrap.get_prediction_levels',
                                                                                                                                            'hierarchicalforecast/probabilistic_methods.py'),
                                                            'hierarchicalforecast.probabilistic_methods.Bootstrap.get_prediction_quantiles': ( 'probabilistic_methods.html#bootstrap.get_prediction_quantiles',
                                                                                                                                               'hierarchicalforecast/probabilistic_methods.py'),
                                                            'hierarchicalforecast.probabilistic_methods.Bootstrap.get_samples': ( 'probabilistic_methods.html#bootstrap.get_samples',
                                                                                                                                  'hierarchicalforecast/probabilistic_methods.py'),
                                                            'hierarchicalforecast.probabilistic_methods.Normality': ( 'probabilistic_methods.html#normality',
                                                                                                                      'hierarchicalforecast/probabilistic_methods.py'),
                                                            'hierarchicalforecast.probabilistic_methods.Normality.__init__': ( 'probabilistic_methods.html#normality.__init__',
                                                                                                                               'hierarchicalforecast/probabilistic_methods.py'),
                                                            'hierarchicalforecast.probabilistic_methods.Normality.get_prediction_levels': ( 'probabilistic_methods.html#normality.get_prediction_levels',
                                                                                                                                            'hierarchicalforecast/probabilistic_methods.py'),
                                                            'hierarchicalforecast.probabilistic_methods.Normality.get_prediction_quantiles': ( 'probabilistic_methods.html#normality.get_prediction_quantiles',
                                                                                                                                               'hierarchicalforecast/probabilistic_methods.py'),
                                                            'hierarchicalforecast.probabilistic_methods.Normality.get_samples': ( 'probabilistic_methods.html#normality.get_samples',
                                                                                                                                  'hierarchicalforecast/probabilistic_methods.py'),
                                                            'hierarchicalforecast.probabilistic_methods.PERMBU': ( 'probabilistic_methods.html#permbu',
                                                                                                                   'hierarchicalforecast/probabilistic_methods.py'),
                                                            'hierarchicalforecast.probabilistic_methods.PERMBU.__init__': ( 'probabilistic_methods.html#permbu.__init__',
                                                                                                                            'hierarchicalforecast/probabilistic_methods.py'),
                                                            'hierarchicalforecast.probabilistic_methods.PERMBU._nonzero_indexes_by_row': ( 'probabilistic_methods.html#permbu._nonzero_indexes_by_row',
                                                                                                                                           'hierarchicalforecast/probabilistic_methods.py'),
                                                            'hierarchicalforecast.probabilistic_methods.PERMBU._obtain_ranks': ( 'probabilistic_methods.html#permbu._obtain_ranks',
                                                                                                                                 'hierarchicalforecast/probabilistic_methods.py'),
                                                            'hierarchicalforecast.probabilistic_methods.PERMBU._permutate_predictions': ( 'probabilistic_methods.html#permbu._permutate_predictions',
                                                                                                                                          'hierarchicalforecast/probabilistic_methods.py'),
                                                            'hierarchicalforecast.probabilistic_methods.PERMBU._permutate_samples': ( 'probabilistic_methods.html#permbu._permutate_samples',
                                                                                                                                      'hierarchicalforecast/probabilistic_methods.py'),
                                                            'hierarchicalforecast.probabilistic_methods.PERMBU.get_prediction_levels': ( 'probabilistic_methods.html#permbu.get_prediction_levels',
                                                                                                                                         'hierarchicalforecast/probabilistic_methods.py'),
                                                            'hierarchicalforecast.probabilistic_methods.PERMBU.get_prediction_quantiles': ( 'probabilistic_methods.html#permbu.get_prediction_quantiles',
                                                                                                                                            'hierarchicalforecast/probabilistic_methods.py'),
                                                            'hierarchicalforecast.probabilistic_methods.PERMBU.get_samples': ( 'probabilistic_methods.html#permbu.get_samples',
                                                                                                                               'hierarchicalforecast/probabilistic_methods.py')},
            'hierarchicalforecast.utils': { 'hierarchicalforecast.utils.CodeTimer': ( 'utils.html#codetimer',
                                                                                      'hierarchicalforecast/utils.py'),
                                            'hierarchicalforecast.utils.CodeTimer.__enter__': ( 'utils.html#codetimer.__enter__',
                                                                                                'hierarchicalforecast/utils.py'),
                                            'hierarchicalforecast.utils.CodeTimer.__exit__': ( 'utils.html#codetimer.__exit__',
                                                                                               'hierarchicalforecast/utils.py'),
                                            'hierarchicalforecast.utils.CodeTimer.__init__': ( 'utils.html#codetimer.__init__',
                                                                                               'hierarchicalforecast/utils.py'),
                                            'hierarchicalforecast.utils.HierarchicalPlot': ( 'utils.html#hierarchicalplot',
                                                                                             'hierarchicalforecast/utils.py'),
                                            'hierarchicalforecast.utils.HierarchicalPlot.__init__': ( 'utils.html#hierarchicalplot.__init__',
                                                                                                      'hierarchicalforecast/utils.py'),
                                            'hierarchicalforecast.utils.HierarchicalPlot.plot_hierarchical_predictions_gap': ( 'utils.html#hierarchicalplot.plot_hierarchical_predictions_gap',
                                                                                                                               'hierarchicalforecast/utils.py'),
                                            'hierarchicalforecast.utils.HierarchicalPlot.plot_hierarchically_linked_series': ( 'utils.html#hierarchicalplot.plot_hierarchically_linked_series',
                                                                                                                               'hierarchicalforecast/utils.py'),
                                            'hierarchicalforecast.utils.HierarchicalPlot.plot_series': ( 'utils.html#hierarchicalplot.plot_series',
                                                                                                         'hierarchicalforecast/utils.py'),
                                            'hierarchicalforecast.utils.HierarchicalPlot.plot_summing_matrix': ( 'utils.html#hierarchicalplot.plot_summing_matrix',
                                                                                                                 'hierarchicalforecast/utils.py'),
                                            'hierarchicalforecast.utils._to_summing_dataframe': ( 'utils.html#_to_summing_dataframe',
                                                                                                  'hierarchicalforecast/utils.py'),
                                            'hierarchicalforecast.utils._to_summing_matrix': ( 'utils.html#_to_summing_matrix',
                                                                                               'hierarchicalforecast/utils.py'),
                                            'hierarchicalforecast.utils.aggregate': ( 'utils.html#aggregate',
                                                                                      'hierarchicalforecast/utils.py'),
                                            'hierarchicalforecast.utils.aggregate_before': ( 'utils.html#aggregate_before',
                                                                                             'hierarchicalforecast/utils.py'),
                                            'hierarchicalforecast.utils.cov2corr': ('utils.html#cov2corr', 'hierarchicalforecast/utils.py'),
                                            'hierarchicalforecast.utils.is_strictly_hierarchical': ( 'utils.html#is_strictly_hierarchical',
                                                                                                     'hierarchicalforecast/utils.py'),
                                            'hierarchicalforecast.utils.numpy_balance': ( 'utils.html#numpy_balance',
                                                                                          'hierarchicalforecast/utils.py')}}}
