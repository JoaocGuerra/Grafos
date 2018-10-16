import unittest
from Roteiro2 import *
from grafo import Grafo as G


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = G(['J', 'C', 'E', 'P', 'M', 'T', 'Z'],
                     {'a1': 'J-C', 'a2': 'C-E', 'a3': 'C-E', 'a4': 'C-P', 'a5': 'C-P', 'a6': 'C-M', 'a7': 'C-T',
                      'a8': 'M-T', 'a9': 'T-Z'})
        self.g_p = convertToMatrizAdj(self.g_p)

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = G(['J', 'C', 'E', 'P', 'M', 'T', 'Z'],
                                   {'a1': 'J-C', 'a3': 'C-E', 'a4': 'C-P', 'a6': 'C-M', 'a7': 'C-T', 'a8': 'M-T',
                                    'a9': 'T-Z'})
        self.g_p_sem_paralelas = convertToMatrizAdj(self.g_p_sem_paralelas)

        # Grafos completos
        self.g_c = G(['J', 'C', 'E', 'P'],
                     {'a1': 'J-C', 'a3': 'J-E', 'a4': 'J-P', 'a6': 'C-E', 'a7': 'C-P', 'a8': 'E-P'})
        self.g_c = convertToMatrizAdj(self.g_c)

        self.g_c2 = G(['J', 'C', 'E', 'P'],
                      {'a1': 'J-C', 'a3': 'E-J', 'a4': 'J-P', 'a6': 'E-C', 'a7': 'C-P', 'a8': 'P-E'})
        self.g_c2 = convertToMatrizAdj(self.g_c2)

        self.g_c3 = G(['J'])
        self.g_c3 = convertToMatrizAdj(self.g_c3)

        # Grafos com laco
        self.g_l1 = G(['A', 'B', 'C', 'D'], {'a1': 'A-A', 'a2': 'B-A', 'a3': 'A-A'})
        self.g_l1 = convertToMatrizAdj(self.g_l1)

        self.g_l2 = G(['A', 'B', 'C', 'D'], {'a1': 'A-B', 'a2': 'B-B', 'a3': 'B-A'})
        self.g_l2 = convertToMatrizAdj(self.g_l2)

        self.g_l3 = G(['A', 'B', 'C', 'D'], {'a1': 'C-A', 'a2': 'C-C', 'a3': 'D-D'})
        self.g_l3 = convertToMatrizAdj(self.g_l3)

        self.g_l4 = G(['D'], {'a2': 'D-D'})
        self.g_l4 = convertToMatrizAdj(self.g_l4)

        self.g_l5 = G(['C', 'D'], {'a2': 'D-C', 'a3': 'C-C'})
        self.g_l5 = convertToMatrizAdj(self.g_l5)

        self.g_l6 = G(['C', 'D'], {'a2': 'D-D', 'a3': 'C-C'})
        self.g_l6 = convertToMatrizAdj(self.g_l6)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(vertices_nao_adjacentes(self.g_p),
                         ['J-J', 'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-C', 'C-Z', 'E-J', 'E-E', 'E-P', 'E-M', 'E-T',
                          'E-Z', 'P-J', 'P-E', 'P-P', 'P-M', 'P-T', 'P-Z', 'M-J', 'M-E', 'M-P', 'M-M', 'M-Z', 'T-J',
                          'T-E', 'T-P', 'T-T', 'Z-J', 'Z-C', 'Z-E', 'Z-P', 'Z-M', 'Z-Z'])

        self.assertEqual(vertices_nao_adjacentes(self.g_p),
                         ['J-J', 'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-C', 'C-Z', 'E-J', 'E-E', 'E-P', 'E-M', 'E-T',
                          'E-Z', 'P-J', 'P-E',
                          'P-P', 'P-M', 'P-T', 'P-Z', 'M-J', 'M-E', 'M-P', 'M-M', 'M-Z', 'T-J', 'T-E', 'T-P', 'T-T',
                          'Z-J', 'Z-C', 'Z-E',
                          'Z-P', 'Z-M', 'Z-Z'])

        self.assertEqual(vertices_nao_adjacentes(self.g_c), ['J-J', 'C-C', 'E-E', 'P-P'])

        self.assertEqual(vertices_nao_adjacentes(self.g_c2), ['J-J', 'C-C', 'E-E', 'P-P'])

        self.assertEqual(vertices_nao_adjacentes(self.g_c3), ['J-J'])

    def test_ha_laco(self):
        self.assertFalse(ha_laco(self.g_p))
        self.assertFalse(ha_laco(self.g_p_sem_paralelas))
        self.assertTrue(ha_laco(self.g_l1))
        self.assertTrue(ha_laco(self.g_l2))
        self.assertTrue(ha_laco(self.g_l3))
        self.assertTrue(ha_laco(self.g_l4))
        self.assertTrue(ha_laco(self.g_l5))

    def test_grau(self):
        # Paraíba
        self.assertEqual(grau(self.g_p, 'J'), 1)
        self.assertEqual(grau(self.g_p, 'C'), 7)
        self.assertEqual(grau(self.g_p, 'E'), 2)
        self.assertEqual(grau(self.g_p, 'P'), 2)
        self.assertEqual(grau(self.g_p, 'M'), 2)
        self.assertEqual(grau(self.g_p, 'T'), 3)
        self.assertEqual(grau(self.g_p, 'Z'), 1)

        # Completos
        self.assertEqual(grau(self.g_c, 'J'), 3)
        self.assertEqual(grau(self.g_c, 'C'), 3)
        self.assertEqual(grau(self.g_c, 'E'), 3)
        self.assertEqual(grau(self.g_c, 'P'), 3)

        # Com laço. Lembrando que cada laço conta uma única vez por vértice para cálculo do grau
        self.assertEqual(grau(self.g_l1, 'A'), 3)
        self.assertEqual(grau(self.g_l2, 'B'), 3)
        self.assertEqual(grau(self.g_l4, 'D'), 1)

    def test_arestas_ha_paralelas(self):
        self.assertTrue(ha_paralelas(self.g_p))
        self.assertFalse(ha_paralelas(self.g_p_sem_paralelas))
        self.assertFalse(ha_paralelas(self.g_c))
        self.assertFalse(ha_paralelas(self.g_c2))
        self.assertFalse(ha_paralelas(self.g_c3))
        self.assertTrue(ha_paralelas(self.g_l1))

    def test_arestas_sobre_vertice(self):
        self.assertEqual(set(arestas_sobre_vertice(self.g_p, 'J')), set(['J-C']))
        self.assertEqual(set(arestas_sobre_vertice(self.g_p, 'C')),
                         set(['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T']))
        self.assertEqual(set(arestas_sobre_vertice(self.g_p, 'M')), set(['C-M', 'M-T']))

    def test_eh_completo(self):
        self.assertFalse(eh_completo(self.g_p))
        self.assertFalse(eh_completo(self.g_p_sem_paralelas))
        self.assertTrue(eh_completo(self.g_c))
        self.assertTrue(eh_completo(self.g_c2))
        self.assertTrue(eh_completo(self.g_c3))
        self.assertFalse(eh_completo(self.g_l1))
        self.assertFalse(eh_completo(self.g_l2))
        self.assertFalse(eh_completo(self.g_l3))
        self.assertTrue(eh_completo(self.g_l4))
        self.assertTrue(eh_completo(self.g_l5))

    """ def teste_conexo(self):
        self.assertTrue(conexo(self.g_p))
        self.assertTrue(conexo(self.g_p_sem_paralelas))
        self.assertTrue(conexo(self.g_c))
        self.assertTrue(conexo(self.g_c2))
        self.assertFalse(conexo(self.g_c3))
        self.assertFalse(conexo(self.g_l1))
        self.assertFalse(conexo(self.g_l2))
        self.assertFalse(conexo(self.g_l3))
        self.assertFalse(conexo(self.g_l6))
        self.assertTrue(conexo(self.g_l4))
        self.assertTrue(conexo(self.g_l5)) """