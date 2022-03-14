# -*- coding: utf-8 -*-

import string
from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date

class escritor(models.Model):
    _name="mis_notas.escritor"
    _description="El que hace las notas"

    name=fields.Char(string="Nombre",required=True)
    surname=fields.Char(string="Apellidos")
    sinCumplir=fields.Integer("Sin cumplir",compute="_get_SinCumplir")

    nota_ids=fields.One2many("mis_notas.nota","escritor_id",string="Notas")

    @api.depends("sinCumplir")
    def _get_SinCumplir(self):
     for escritor in self:
       for nota in escritor.nota_ids:
           if nota.cumplido:
               escritor.sinCumplir=escritor.sinCumplir
           else:
               escritor.sinCumplir+=1    




class nota(models.Model):
    _name="mis_notas.nota"
    _description="La nota"

    name=fields.Char(string="Nombre",required=True)
    texto=fields.Text(string="TextoNota",required=True)
    fecha=fields.Date(string="Fecha escritura",default=date.today())
    dias=fields.Integer("Días escrita",compute="_get_dias")
    cumplido=fields.Boolean("Cumplido",default=False)
    escritor_id=fields.Many2one("mis_notas.escritor",string="Escritor",required=True)

    @api.depends("fecha")
    def _get_dias(self):
     for nota in self:
        hoy=date.today()
        nota.dias=relativedelta(hoy, nota.fecha).days

# class mis_notas(models.Model):
#      _name = 'mis_notas.mis_notas'
#      _description = 'mis_notas.mis_notas'

#      name = fields.Char()
#      value = fields.Integer()
#      value2 = fields.Float(compute="_value_pc", store=True)
#      description = fields.Text()

#      @api.depends('value')
#      def _value_pc(self):
#          for record in self:
#              record.value2 = float(record.value) / 100
