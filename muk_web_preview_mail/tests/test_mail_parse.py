# -*- coding: utf-8 -*-

###################################################################################
#
#    Copyright (C) 2017 MuK IT GmbH
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

import base64
import unittest

from odoo import _
from odoo.tests import common

from .. import controllers

class MailParseTestCase(common.TransactionCase):
    
    at_install = False
    post_install = True
    
    def setUp(self):
        super(MailParseTestCase, self).setUp()
        self.attachment_model = self.env['ir.attachment'].sudo()
        self.sample_mail_attachment = self.attachment_model.create({
            'name': 'SampleMail',
            'datas': base64.encodestring(""" 
                Return-Path: <mlemos@acm.org>
                To: Manuel Lemos <mlemos@linux.local>
                Subject: Testing Manuel Lemos' MIME E-mail composing and sending PHP class: HTML message
                From: mlemos <mlemos@acm.org>
                Reply-To: mlemos <mlemos@acm.org>
                Sender: mlemos@acm.org
                X-Mailer: http://www.phpclasses.org/mimemessage $Revision: 1.63 $ (mail)
                MIME-Version: 1.0
                Content-Type: multipart/mixed; boundary="652b8c4dcb00cdcdda1e16af36781caf"
                Message-ID: <20050430192829.0489.mlemos@acm.org>
                Date: Sat, 30 Apr 2005 19:28:29 -0300
                
                
                --652b8c4dcb00cdcdda1e16af36781caf
                Content-Type: multipart/related; boundary="6a82fb459dcaacd40ab3404529e808dc"
                
                
                --6a82fb459dcaacd40ab3404529e808dc
                Content-Type: multipart/alternative; boundary="69c1683a3ee16ef7cf16edd700694a2f"
                
                
                --69c1683a3ee16ef7cf16edd700694a2f
                Content-Type: text/plain; charset=ISO-8859-1
                Content-Transfer-Encoding: quoted-printable
                
                This is an HTML message. Please use an HTML capable mail program to read
                this message.
                
                --69c1683a3ee16ef7cf16edd700694a2f
                Content-Type: text/html; charset=ISO-8859-1
                Content-Transfer-Encoding: quoted-printable
                
                <html>
                <head>
                <title>Testing Manuel Lemos' MIME E-mail composing and sending PHP class: H=
                TML message</title>
                <style type=3D"text/css"><!--
                body { color: black ; font-family: arial, helvetica, sans-serif ; backgroun=
                d-color: #A3C5CC }
                A:link, A:visited, A:active { text-decoration: underline }
                --></style>
                </head>
                <body>
                <table background=3D"cid:4c837ed463ad29c820668e835a270e8a.gif" width=3D"100=
                %">
                <tr>
                <td>
                <center><h1>Testing Manuel Lemos' MIME E-mail composing and sending PHP cla=
                ss: HTML message</h1></center>
                <hr>
                <P>Hello Manuel,<br><br>
                This message is just to let you know that the <a href=3D"http://www.phpclas=
                ses.org/mimemessage">MIME E-mail message composing and sending PHP class</a=
                > is working as expected.<br><br>
                <center><h2>Here is an image embedded in a message as a separate part:</h2>=
                </center>
                <center><img src=3D"cid:ae0357e57f04b8347f7621662cb63855.gif"></center>Than=
                k you,<br>
                mlemos</p>
                </td>
                </tr>
                </table>
                </body>
                </html>
                --69c1683a3ee16ef7cf16edd700694a2f--
                
                --6a82fb459dcaacd40ab3404529e808dc
                Content-Type: image/gif; name="logo.gif"
                Content-Transfer-Encoding: base64
                Content-Disposition: inline; filename="logo.gif"
                Content-ID: <ae0357e57f04b8347f7621662cb63855.gif>
                
                R0lGODlhlgAjAPMJAAAAAAAA/y8vLz8/P19fX19f339/f4+Pj4+Pz7+/v///////////////////
                /////yH5BAEAAAkALAAAAACWACMAQwT+MMlJq7046827/2AoHYChGAChAkBylgKgKClFyEl6xDMg
                qLFBj3C5uXKplVAxIOxkA8BhdFCpDlMK1urMTrZWbAV8tVS5YsxtxmZHBVOSCcW9zaXyNhslVcto
                RBp5NQYxLAYGLi8oSwoJBlE+BiSNj5E/PDQsmy4pAJWQLAKJY5+hXhZ2dDYldFWtNSFPiXssXnZR
                k5+1pjpBiDMJUXG/Jo7DI4eKfMSmxsJ9GAUB1NXW19jZ2tvc3d7f4OHi2AgZN5vom1kk6F7s6u/p
                m3Ab7AOIiCxOyZuBIv8AOeTJIaYQjiR/kKTr5GQNE3pYSjCJ9mUXClRUsLxaZGciC0X+OlpoOuQo
                ZKdNJnIoKfnxRUQh6FLG0iLxIoYnJd0JEKISJyAQDodp3EUDC48oDnUY7HFI3wEDRjzycQJVZCQT
                Ol7NK+G0qgtkAcOKHUu2rNmzYTVqRMt2bB49bHompSchqg6HcGeANSMxr8sEa2y2HexnSEUTuWri
                SSbkYh7BgGVAnhB1b2REibESYaRoBgqIMYx59tFM9AvQffVG49P5NMZkMlHKhJPJb0knmSKZ6kSX
                JtbeF3Am7ocok6c7cM7pU5xcXiJJETUz16qPrzEfaFgZpvzn7h86YV5r/1mxXeAUMVyEIpnVUGpN
                RlG2ka9b3lP3pm2l6u7P+l/YLj3+RlEHbz1C0kRxSITQaAcilVBMEzmkkEQO8oSOBNg9SN+AX6hV
                z1pjgJiAhwCRsY8ZIp6xj1ruqCgeGeKNGEZwLnIwzTg45qjjjjz2GEA5hAUp5JBEFmnkkSCoWEcZ
                X8yohZNK1pFGPQS4hx0qNSLJlk9wCQORYu5QiMd7bUzGVyNlRiOHSlpuKdGEItHQ3HZ18beRRyws
                YSY/waDTiHf/tWlWUBAJiMJ1/Z0XXU7N0FnREpKM4NChCgbyRDq9XYpOplaKopN9NMkDnBbG+UMC
                QwLWIeaiglES6AjGARcPHCWoVAiatcTnGTABZoLPaPG1phccPv366mEvWEFSLnj+2QaonECwcJt/
                e1Zw3lJvVMmftBdVNQS3UngLCA85YHIQOy6JO9N4eZW7KJwtOUZmGwOMWqejwVW6RQzaikRHX3yI
                osKhDAq8wmnKSmdMwNidSOof9ZG2DoV0RfTVmLFtGmNk+CoZna0HQnPHS3AhRbIeDpqmR09E0bsu
                soeaw994z+rwQVInvqLenBftYjLOVphLFHhV9qsnez8AEUbQRgO737AxChjmyANxuEFHSGi7hFCV
                4jxLst2N8sRJYU+SHiAKjlmCgz2IffbLI5aaQR71hnkxq1ZfHSfKata6YDCJDMAQwY7wOgzhjxgj
                VFQnKB5uX4mr9qJ79pann+VcfcSzsSCd2mw5scqRRvlQ6TgcUelYhu75iPE4JejrsJOFQAG01277
                7bjnrvvuvPfu++/ABy887hfc6OPxyCevPDdAVoDA89BHL/301Fdv/fXYZ6/99tx3Pz0FEQAAOw==
                
                --6a82fb459dcaacd40ab3404529e808dc
                Content-Type: image/gif; name="background.gif"
                Content-Transfer-Encoding: base64
                Content-Disposition: inline; filename="background.gif"
                Content-ID: <4c837ed463ad29c820668e835a270e8a.gif>
                
                R0lGODlh+wHCAPMAAKPFzKLEy6HDyqHCyaDByJ/Ax56/xp2+xZ28xJy7w5u6wpq5wZm4wJm3v5i2
                vpe1vSwAAAAA+wHCAEME/hDISau9OOvNu/9gKI5kaZ5oqq5s675wLM90bd94ru987//AoHBILBqP
                yKRyyWw6n9CodEqtWq+gwSHReHgfjobY8X00FIc019tIHAYS7dqcQCDm3vC4fD4QAhUBBFsMZF8O
                hnkLCAYFW11tb1iTlJWWOXJdZZtmC24Eg3hgYntfbXainJ2fgBSZbG5wFAG0E6+RoAZ3CbwJCgya
                p3cMbAyevQcFAgMGCcRmxr1uyszOxQq+wF4MdcPFx7zJApfk5eYhr3SSGemRsu3dc+4iAqELhZwO
                0X6hkHUHCBRoGtUg0RkEAAUeKhhGAcICBQIODIPooIEBzCTmKcjGYSNd/go3VvQo65zJkyhTqlzJ
                sqXLlzBjypxJs6bNmzhz6tzJs6fPn0CDCh1KtKjRo0iTKl3KtKnTp1CXBhhAwECaq1gPNCIwANDU
                qmkMcG311apWULmyZt3alcPXAma1FgAlgCxVq2LbRt3LF0Y7hwWoEjLEDZUmff8AOjMkTB5gwYu3
                JbhIQUDEZw+4+aE1aNc0R2vcDYjoDBgpBoUDj95yzzRqbH7qgW4t5vUnAfVAoj7NwOOf1QloN7Ad
                u1Xf41b+IlCNsa6rR7DWwTPccTnG5sYvCEKwgPGiZI64A9OsK/Q/BM/0YfuFz13VOwsULLhHps+f
                98Hl0zeDRk0X9Qih/vLPWPjFN197aPyB3IJVBLDMdc5t4OB1A0QowYQQ0vIgdilgyGEgG1roYV0j
                GufhhyBSWGF2s2yIYosqWsjgjDTWaOONOOao44489ujjj0AGKeSQRBZp5JFIJqnkkkw26eSTUMJU
                llpYseXVXWGNdSGWZ6EVF5VWukUVXFdtRUCEU+bFYpRslqNcYKHgk1k8hxWWxjCM0VkdnINJRtkE
                lqH3hWZ/CKJYOBBBJxppu/FWh2qzNUrcmQRE6lpvt+UWUKPD9cbIb5bWhmlxbbL5JoUywiMddHRQ
                x591GWqwXXdsfJeoeMO5UZ4/AaaHKXv1xVKgfghuNuyB9fUHHYAA/u2CEIHlGbiffWuWyuSJMmKA
                bXbbbtuhi9kCUOIEJY57oYsraoduuOfGWO2J6Vor77z01mvvvfjmq+++/Pbr778AByzwwAQXbPDB
                CCfcZDobldLRVfLEEgerjQ1EEEemJMiioZEdkggYizSiqMQKl5wCw6qswg+rDTvc6h0Wq9KAJ5tV
                oGpJF9YysXn8lCfNL8HE88xw4EyzTDNDR4MMNUhfk40mhXkDTdHimHzjzRpgDcB0MEeHswf1sCZn
                GfrQDMrIAYZEkEEOJTQRQweBp5FIDTGCEUiHYWwRXHOPMpLdVgcu+OCEF2744YgnrvjijDfu+OOQ
                Ry755JRXbvnl/phnrvnmnHfu+eegZ57RAqSUzptv75E+M+Bb66L6InZwZ7rpr31aLQBhb2pap548
                e7TsIX8dOr/pIIZQQphFHfGqEbtq/J2/DDrZ13Ga0jt8h/XX9TxvfRmmuPVUatb34INCplxakjtm
                XOQ7aP74c+k1fE4MD7fefvxBbLEeLldsyq/4o9ZzHOOHylBFS7f4RJxQMx/8MeB4ggIDA02ziLno
                wlfGoOByKnUAhZQNWfkzwAXzMEExVFB+86NJ/TDVC4SIZRzFs5Ni5OQ/p7XwLOOwQDXSswgFiYuD
                Z4GMP8AjtvGgJk9aYU2davdCeyzRU2LpBwkb2KjvWCU4T/TN/u1S+BKtYUBrXFue8DYQKFoVAzXa
                eJh/XiYPpZEOFhAMTnzkk8aQWQU+c7yHJkIGkGd4SkDhMJ9i5qMAOu4RAWfiYk1yxwvfaYCRA8oh
                JF14x0bGhgSyaZY07JCMRDLyWWnxTOyc1UmweMaSL5zSKf/xQgnk5lA3TCWWVunCRCrylrjMpS53
                ycte+vKXwAymMIdJzGIa85jITKYyl8nMZjrzmdCMpjSnSc1qWvOa2MymvkY3u9IxMReyW92fuLm6
                2Kmum53SIgZyxx7e9C423AyeNnkUw8RsSnqumsfWKKYnCdozen6iHiGsF483gkF7PIND96oUP7KE
                73zteyj8/tK3JfGVqaHkkmhYMDrPJqzwfjRUlij4hzE4ds1pdGSMxgYYjAQZEBRtSeDKSmMMEGYG
                ghjU4+osGEF9ZNCEG3SEB2s6LTSIsKcl3CkKO2qEj24Sh/ucw/NmmCdXQQMbsbSlzZoGMkSSBYh5
                kWIkEhWc3aARiVc0qE+hSCklkvCbUpQgFTWYRCy+la1bZGoQvHgBMPIznyT7QBkNgsY05m+NNSQa
                Lwx6ijvJsZB69IIdB5nHOjKij9twCCAVGJ7HGlKyiMyhXo0wyUtmoLS2LK0ID+XIEWRys5ycyzg+
                yQ9TtjB2lpyLbZ8qy91mVZK+ReWZVCkNVmp1tMhNrnKX/svc5jr3udCNrnSnS93qWve62M2udrfL
                3e5697vgDa94x0ve8pr3vOhNr3rXy972uve98I2vfOdLXxrBS0Uv8lZGUaUh/OKXXRmAV7jMVV+X
                QLK4vD0TaoHLWq1UEsEJFu0FXknLh3iyM5EssEtQlrK98ZN5QbNqyl71pwqEza752MfZEqrhljg1
                pYMKkBh3FuKTXtUX+LupMkwcETNCA40D6QNiA3tfdunXAkdOEX+1Ba68tjiqLbVOnKp60oNAam6J
                fcyUvTYLAnDHOw8Jjx7Js71YTKWzxX1IV76iyayuWTCwDSIgKJxmqLI5zmp6sg5ZNdV7bkPGQWYh
                0EzR/s8+A1THEt6hIrx6IbByRawKHKjfpEfExVREpUEdzKX3dJe5UaQ6UdT0p18VGCfPF2X8S4QD
                QgaamI24hi1TtTxZyuVZ6AzK6gBnIbE66DmhImlzxAYouUq0XQ+oUhG039P+rAZgG7u1erYFyy6W
                Tt85ddkmHak3PWVaWuePAC9F4Mh6dgdjB/A8tCqbscUxWLmumxp8jsa5A5RuY7xbwtHGtT+Phz69
                nGo0WC60DPt9u0AljxWG8kylh9hsRKw1jbiwx24cDsUKSRwYFPdIq2347NoWkSEAKnG++brnGes7
                sYH1QPVqVdDsOZZXUlN2WYO1soCA9JBoScjNQdvs/n3fKXaxYefOH9BDfD+Z5Db78Dv+WuWUd4Bj
                YwPDx1bNiI03BoO7yRi9CzJBBLlQdj5tTbKIOFQqikHjruN6Bovlw5GnXZxjtMXbZ01O2NnhdawL
                ASOFw8BIxpOSuutUYWfmBjW0U1S+gczhqy0Wzuhmd7Ur5RYW/01Tz3dKcpYVl/Isrs2jBSyZJ4H7
                LIq+4VYUL2NZaCMgQiY1LXSjFH09wWexvovGvvawX2q+d8/73vv+98APvvCHT/ziG//4yE++8pfP
                /OY7//nQj770p0/96lv/+tjPvva3z/3ue//74A+/+MdP/vKb//zoT7/6e3Lf/3KryTDKUPvdBQIB
                /q+JwOuPwYEhbFzcYDjDuPN/lARL/FdLRlcZwdUNnTRbGAZt+fcCHCYzGqd0NJZtrsYJFjFGJ2ZQ
                m1A2kcZiD+gXLKNsMMZsTQdiFvg/IJUID7RjldFjhAVkGaM/6lASRfYu8KcuS6aDO4hkOfh7p7Jl
                bBRlVxYSWSZlfVKDXfZltRJmADFmulJmb3BmBJhbb9YZp1RLV9hmwtUWdBZhnYeFCaZ7Rxdv/5Q8
                gKaCvNBrQ0hCZxhjLhgHXEV1PiQIjhBEkDZT6VFSmkFWhbBppMZBljZqVtZpIUGIqCNqevMYlhdf
                qEYKslZ10zZibbgQDkN1IndyTkcLxiFTulZI/muYRsrjbKA4bNYwNR1nPsn2K6J4PKdYbKXYbSM3
                bSQVeWdybWwIa9Rmi0b3FwUEKAcUU+MGTr4AivP2hGSgbqDIbjDobssIb1IlbzSEbslob894gGUY
                jYkxeyf3GABnhAK3jeTDYxE0J5uRcEtjdYUnaoMXHStGGxlnNxs4cYgARRt3Y8UobB5XVhhXjyTR
                e0jnbfoURkGzDh+wcquACmqFUDD3iiw0LZFmczhmWTknkZ9FdK5IDH0GdArWGaB4kUXHewEpbSZH
                kLX2AVA3dVPHamgjNQ8XZG0Ddl2XLF9HOmF3RPmTKGV3IGdXdWl3k2zXiPBVd3nXV3PHOkRpgk5A
                lYlgg2F8Fw3WlnZW9HiCB2Q0Y3ic8k2Kl5V4JQhUiXgWFgqUh1e9h3mcpy2epxdm+XnjQ1EiMHoQ
                pVtogiWuV3urBxGod4Xnw41huJfjKHvtg3t8GYKEWZiGeZiImZiKuZiM2ZiO+ZiQGZmSOZmUWZmW
                eZmYmZmauZmc2ZlCEQEAOw==
                
                --6a82fb459dcaacd40ab3404529e808dc--
                
                --652b8c4dcb00cdcdda1e16af36781caf
                Content-Type: text/plain; name="attachment.txt"
                Content-Transfer-Encoding: base64
                Content-Disposition: attachment; filename="attachment.txt"
                
                VGhpcyBpcyBqdXN0IGEgcGxhaW4gdGV4dCBhdHRhY2htZW50IGZpbGUgbmFtZWQgYXR0YWNobWVu
                dC50eHQgLg==
                
                --652b8c4dcb00cdcdda1e16af36781caf--
            """)
        })

    def tearDown(self):
        super(MailParseTestCase, self).tearDown()
        
    def test_parse_mail(self):
        assertTrue(controllers.main.MailParserController().parse_mail('/web/content/%s?download=true' % self.sample_mail_attachment.id))
    
        