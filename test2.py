#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import re
data='''
						<div id="c461" class="csc-default"><div class="csc-header csc-header-n1"><h1 class="csc-firstHeader">World Parliamentarian’s Convention on Tibet in Rome </h1></div><div class="csc-text-content"><p><b>16 november 2009</b>
</p>
<p>     <br />   
</p>
<p>De 5e ‘’World Parliamentarian’s Convention on Tibet’’ (WPCT) vond op 17, 18 en 19 november plaats in Rome en bracht internationale parlementariërs samen die betrokken zijn bij Tibetaanse zaken.&nbsp; De Dalai Lama hield de openingstoespraak.<br /><br /><img src="uploads/RTEmagicC_copy_of_dsc_1516_03.jpg.jpg" width="450" height="300" alt="" /><br /><br />De 5e WPCT werd georganiseerd door de Italiaanse Parlementaire Tibet Intergroup in samenwerking met het Tibetaanse Parlement in Ballingschap en Internati'''
print(re.findall(re.compile(r'\d{0,2} \d{4}'), data))
r'<i>28 december 2009</i>'
r'<b>28 december 2009</b>'
r'<p>28 december 2009</p>'

print(re.findall(re.compile(r'\d{0,2} \d{4}'), data))

