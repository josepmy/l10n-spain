# © 2016 Serv. Tecnol. Avanzados - Pedro M. Baeza
# © 2017 Creu Blanca
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from .common import CommonTest


class TestL10nEsFacturae321(CommonTest):
    def setUp(self):
        super().setUp()
        self.partner.facturae_version = '3_2_1'
        self.fe = 'http://www.facturae.es/Facturae/2014/v3.2.1/Facturae'
        self.first_check_amount = [
            '190.31000000', '190.31000000', '190.31000000', '39.96594000'
        ]
        self.second_check_amount = [
            '190.31000000', '133.22000000', '133.22000000', '27.97615800'
        ]
