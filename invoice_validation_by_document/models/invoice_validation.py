from odoo import api, fields, models


class InvoiceValidationDocument(models.Model):
    _inherit = "l10n_latam.identification.type"

    invoice_validation_document = fields.Many2many(
        string='Comprobantes de pago aceptados',
        relation="relation_invoice_validation_dccument",
        comodel_name='l10n_latam.document.type'
    )

"""

class AccountMove(models.Model):

    _inherit = "account.move"

    l10n_latam_document_type_id = fields.Many2one(
        readonly=True,
        domain="[('id', 'in', invoice_validation_document)]"
    )

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id.company_type == 'person':
            document = self.env['l10n.latam.document.type'].search(['name', '=', 'Boleta'])
            self.l10n_latam_document_type_id.id = document
        else:
            self.move_type = 'in invoice'
            super(_onchange_partner_id, self)
"""