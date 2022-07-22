# Author: Michael Coughlin
import csv
import os
import sys

authors = [
{'name': 'S.~Agayeva', 'affiliations': ['N.Tusi Shamakhy Astrophysical Observatory Azerbaijan National Academy of Sciences, settl.Y. Mammadaliyev, AZ 5626, Shamakhy, Azerbaijan'], 'email': 'sebnem-agayeva-94@MAIL.RU'},
{'name': 'V.~Aivazyan', 'affiliations': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia', 'Samtskhe-Javakheti  State  University, Rustaveli Str. 113,  Akhaltsikhe, 0080,  Georgia'], 'email': 'vovaaivazian10@GMAIL.COM'},
{'name': 'S.~Alishov', 'affiliations': ['N.Tusi Shamakhy astrophysical Observatory Azerbaijan National Academy of Sciences, settl.Mamedaliyev, AZ 5626, Shamakhy, Azerbaijan'], 'email': 'sebaheddin.ali@GMAIL.COM'},
{'name': 'M.~Almualla', 'affiliations': ['American University of Sharjah, Physics Department, PO Box 26666, Sharjah, UAE'], 'email': 'g00074394@aus.edu'},
{'name': 'C.~Andrade', 'affiliations': ['School of Physics and Astronomy, University of Minnesota, Minneapolis, Minnesota 55455, USA'], 'email': 'andra104@UMN.EDU'},
{'name': 'S.~Antier', 'affiliations': ["Artemis, Observatoire de la C\\^ote d’Azur, Universit\\'e C\\^ote d’Azur, Boulevard de l'Observatoire, 06304 Nice, France"], 'email': 'sarah.antier@OCA.EU'},
{'name': 'J.-M.~Bai', 'affiliations': ['Yunnan Observatories, Chinese Academy of Sciences, Kunming 650011, Yunnan Province, People’s Republic of China'], 'email': 'baijm@163.net'},
{'name': 'A.~Baransky', 'affiliations': ['Astronomical Observatory Taras Shevshenko National University of Kyiv, Observatorna str. 3, Kyiv, 04053, Ukraine'], 'email': 'abaransky@UKR.NET'},
{'name': 'S.~Basa', 'affiliations': ['Aix Marseille Univ, CNRS, CNES, LAM, IPhU, Marseille, France'], 'email': 'Stephane.Basa@LAM.FR'},
{'name': 'P.~Bendjoya', 'affiliations': ['Laboratoire J.-L. Lagrange, Universit de Nice Sophia-Antipolis, CNRS, Observatoire de la Cote d’Azur, F-06304 Nice, France'], 'email': 'bendjoya@oca.eu'},
{'name': 'Z.~Benkhaldoun', 'affiliations': ['Universit ́e Cadi Ayyad, Facult ́e des Sciences Semlalia, Av. Prince My Abdellah, BP 2390 Marrakesh, Morocco'], 'email': 'zouhair@uca.ac.ma'},
{'name': 'S.~Beradze', 'affiliations': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia', 'Samtskhe-Javakheti  State  University, Rustaveli Str. 113,  Akhaltsikhe, 0080,  Georgia'], 'email': 'beradze.sophia@GMAIL.COM'},
{'name': 'D.~Berezin', 'affiliations': ['ICAMER Observatory of NAS of Ukraine 27 Acad. Zabolotnoho Str., Kyiv, 03143, Ukraine'], 'email': ''},
{'name': 'U.~Bhardwaj', 'affiliations': ['GRAPPA, Anton Pannekoek Institute for Astronomy and Institute of High-Energy Physics, University of Amsterdam, Science Park 904,1098 XH Amsterdam, The Netherlands'], 'email': 'u.bhardwaj@UVA.NL'},
{'name': 'M.~Blazek', 'affiliations': ["Instituto de Astrof\\'isica de Andaluc\\'ia (IAA-CSIC), Glorieta de la Astronom\\'ia s/n, 18008 Granada, Spain"], 'email': 'embee.cz@GMAIL.COM'},
{'name': 'O.~Burkhonov', 'affiliations': ['Ulugh Beg Astronomical Institute, Uzbekistan Academy of Sciences, Astronomy str. 33, Tashkent 100052, Uzbekistan'], 'email': 'boa@ASTRIN.UZ'},
{'name': 'E.~Burns', 'affiliations': ['Department of Physics \\& Astronomy, Louisiana State University, Baton Rouge, LA 70803, USA'], 'email': 'ericburns@lsu.edu'},
{'name': 'S.~Caudill', 'affiliations': ['Institute for Gravitational and Subatomic Physics (GRASP), Utrecht University, Princetonplein 1, 3584 CC, Utrecht, The Netherlands', 'Nikhef, Science Park 105, 1098 XG, Amsterdam, The Netherlands'], 'email': 's.caudill@NIKHEF.NL'},
{'name': 'N.~Christensen', 'affiliations': ["Artemis, Observatoire de la C\\^ote d’Azur, Universit\\'e C\\^ote d’Azur, Boulevard de l'Observatoire, 06304 Nice, France"], 'email': 'nelson.christensen@OCA.EU'},
{'name': 'F.~Colas', 'affiliations': ["Astronomie et Syst\\`emes Dynamiques, Institut de M\\'ecanique C\\'eleste et de Calcul des \\'Eph\\'em\\'erides CNRS UMR 8028, Observatoire de Paris, Universit\\'e PSL, Sorbonne Universit\\'e, 77 Avenue Denfert-Rochereau, 75014 Paris, France"], 'email': 'francois.colas@obspm.fr'},
{'name': 'A.~Coleiro', 'affiliations': ["Universit\\'e Paris Cit\\'e, CNRS, Astroparticule et Cosmologie, F-75013 Paris, France"], 'email': 'coleiro@APC.IN2P3.FR'},
{'name': 'W.~Corradi', 'affiliations': ["Laborat\\'orio Nacional de Astrofísica, R. dos Estados Unidos, 154 - Nações, Itajub\\'a - MG, 37504-364, Brazil"], 'email': 'wbcorradi@LNA.BR'},
{'name': 'M.~W.~Coughlin', 'affiliations': ['School of Physics and Astronomy, University of Minnesota, Minneapolis, Minnesota 55455, USA'], 'email': 'michael.w.coughlin@GMAIL.COM'},
{'name': 'T.~Culino', 'affiliations': ["Artemis, Observatoire de la C\\^ote d’Azur, Universit\\'e C\\^ote d’Azur, Boulevard de l'Observatoire, 06304 Nice, France"], 'email': 'thomas.culino@EDU.DEVINCI.FR'},
{'name': 'D.~Darson', 'affiliations': ['Ecole Normale Superieure, CNRS-PSL, Research University, 45, rue d’Ulm 75230 Paris Cedex 5 France'], 'email': ''},
{'name': 'D.~Datashvili', 'affiliations': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia', 'Samtskhe-Javakheti  State  University, Rustaveli Str. 113,  Akhaltsikhe, 0080,  Georgia'], 'email': 'datashvili.data@YAHOO.COM'},
{'name': 'G.~de~Wasseige', 'affiliations': ['Centre for Cosmology, Particle Physics and Phenomenology - CP3, Universite Catholique de Louvain, B-1348 Louvain-la-Neuve, Belgium'], 'email': 'gwenhael.dewasseige@UCLOUVAIN.BE'},
{'name': 'T.~Dietrich', 'affiliations': ['Institute for Physics and Astronomy, University of Potsdam, D-14476 Potsdam, Germany', 'Max Planck Institute for Gravitational Physics (Albert Einstein Institute), Am M{\\"u},hlenberg 1, D-14476, Germany'], 'email': 'tim.dietrich@UNI-POTSDAM.DE'},
{'name': 'F.~Dolon', 'affiliations': ["OHP, Observatoire de Haute-Provence, CNRS, Aix Marseille University, Institut Pyth\\'eas, St Michel l’Observatoire, France"], 'email': ''},
{'name': 'D.~Dornic', 'affiliations': ['CPPM, Aix Marseille Univ, CNRS/IN2P3, CPPM, Marseille, France'], 'email': 'dornic@CPPM.IN2P3.FR'},
{'name': 'J.~Dubouil', 'affiliations': ["Astronomie et Syst\\`emes Dynamiques, Institut de M\\'ecanique C\\'eleste et de Calcul des \\'Eph\\'em\\'erides CNRS UMR 8028, Observatoire de Paris, Universit\\'e PSL, Sorbonne Universit\\'e, 77 Avenue Denfert-Rochereau, 75014 Paris, France"], 'email': 'Julien.Dubouil@OBSPM.FR'},
{'name': 'J.-G.~Ducoin', 'affiliations': ['Institut d’Astrophysique de Paris, 98 bis boulevard Arago, 75014 Paris, France'], 'email': 'ducoin@IAP.FR'},
{'name': 'P.-A.~Duverne', 'affiliations': ['IJCLab, Univ Paris-Saclay, CNRS/IN2P3, Orsay, France'], 'email': 'pierre-alexandre.duverne@U-PSUD.FR'},
{'name': 'A.~Esamdin', 'affiliations': ['Xinjiang Astronomical Observatory, Chinese Academy of Sciences, Urumqi, Xinjiang 830011, People’s Republic of China', 'University of Chinese Academy of Sciences, Beijing 100049, People’s Republic of China'], 'email': 'aliyi@xao.ac.cn'},
{'name': 'A.~Fouad', 'affiliations': ['National Research Institute of Astronomy and Geophysics, 1 El-marsad St., Helwan, Cairo, Egypt'], 'email': 'ahmed.fouad@nriag.sci.eg'},
{'name': 'F.~Guo', 'affiliations': ['Physics Department and Astronomy Department, Tsinghua University, Beijing, 100084, People’s Republic of China'], 'email': 'gfz20@MAILS.TSINGUA.EDU.CN'},
{'name': 'V.~Godunova', 'affiliations': ['ICAMER Observatory of NAS of Ukraine 27 Acad. Zabolotnoho Str., Kyiv, 03143, Ukraine'], 'email': 'godunova@MAO.KIEV.UA'},
{'name': 'P.~Gokuldass', 'affiliations': ['Department of Aerospace, Physics, and Space Sciences, Florida Institute of Technology, Melbourne, Florida 32901, USA'], 'email': 'priyadass.94@GMAIL.COM'},
{'name': 'N.~Guessoum', 'affiliations': ['American University of Sharjah, Physics Department, PO Box 26666, Sharjah, UAE'], 'email': 'nguessoum@AUS.EDU'},
{'name': 'E.~Gurbanov', 'affiliations': ['N.Tusi Shamakhy Astrophysical Observatory Azerbaijan National Academy of Sciences, settl.Y. Mammadaliyev, AZ 5626, Shamakhy, Azerbaijan'], 'email': 'emingurban88@GMAIL.COM'},
{'name': 'R.~Hainich', 'affiliations': ['Institut f\\"ur Physik und Astronomie, Universit\\"at Potsdam, Karl-Liebknecht-Str. 24/25, D-14476 Potsdam, Germany'], 'email': 'rhainich@ASTRO.PHYSIK.UNI-POTSDAM.DE'},
{'name': 'E.~Hasanov', 'affiliations': ['N.Tusi Shamakhy Astrophysical Observatory Azerbaijan National Academy of Sciences, settl.Y. Mammadaliyev, AZ 5626, Shamakhy, Azerbaijan'], 'email': 'emrah.hesenov.2020@GMAIL.COM'},
{'name': 'P.~Hello', 'affiliations': ['IJCLab, Univ Paris-Saclay, CNRS/IN2P3, Orsay, France'], 'email': 'patrice.hello@IJCLAB.IN2P3.FR'},
{'name': 'T.~Hussenot-Desenonges', 'affiliations': ['IJCLab, Univ Paris-Saclay, CNRS/IN2P3, Orsay, France'], 'email': 'thomas.hussenot@ijclab.in2p3.fr'},
{'name': 'R.~Inasaridze', 'affiliations': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia', 'Samtskhe-Javakheti  State  University, Rustaveli Str. 113,  Akhaltsikhe, 0080,  Georgia'], 'email': 'innasaridze@YAHOO.COM'},
{'name': 'A.~Iskandar', 'affiliations': ['Xinjiang Astronomical Observatory, Chinese Academy of Sciences, Urumqi, Xinjiang 830011, People’s Republic of China'], 'email': 'abudu@XAO.AC.CN'},
{'name': 'E.~E.~O.~Ishida', 'affiliations': ["LPC, Universit\\'e Clermont Auvergne, CNES/IN2P3, F-63000, France"], 'email': 'emilleishida@gmail.com'},
{'name': 'N.~Ismailov', 'affiliations': ['N.Tusi Shamakhy Astrophysical Observatory Azerbaijan National Academy of Sciences, settl.Y. Mammadaliyev, AZ 5626, Shamakhy, Azerbaijan'], 'email': 'ismailovnshao@GMAIL.COM'},
{'name': 'T.~Jegou~du~Laz', 'affiliations': ['IJCLab, Univ Paris-Saclay, CNRS/IN2P3, Orsay, France'], 'email': 'theophile.jegou_du_laz@EDU.DEVINCI.FR'},
{'name': 'D.~A.~Kann', 'affiliations': ["Instituto de Astrof\\'isica de Andaluc\\'ia (IAA-CSIC), Glorieta de la Astronom\\'ia s/n, 18008 Granada, Spain"], 'email': 'kann@iaa.es'},
{'name': 'G.~Kapanadze', 'affiliations': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia', 'Samtskhe-Javakheti  State  University, Rustaveli Str. 113,  Akhaltsikhe, 0080,  Georgia'], 'email': 'kapanadzegivi@GMAIL.COM'},
{'name': 'S.~Karpov', 'affiliations': ['FZU - Institute of Physics of the Czech Academy of Sciences, Na Slovance 1999/2, CZ-182 21, Praha, Czech Republic'], 'email': 'karpov@FZU.CZ'},
{'name': 'R.~W.~Kiendrebeogo', 'affiliations': ["Artemis, Observatoire de la C\\^ote d’Azur, Universit\\'e C\\^ote d’Azur, Boulevard de l'Observatoire, 06304 Nice, France", "Laboratoire de Physique et de Chimie de l’Environnement, Universit\\'e Joseph KI-ZERBO, Ouagadougou, Burkina Faso"], 'email': 'weizmann.kiendrebeogo@OCA.EU'},
{'name': 'A.~Klotz', 'affiliations': ["IRAP, Universit\\'e de Toulouse, CNRS, UPS, 14 Avenue Edouard Belin, F-31400 Toulouse, France", "Universit\\'e Paul Sabatier Toulouse III, Universit'e de Toulouse, 118 route de Narbonne, 31400 Toulouse, France"], 'email': 'aklotz@IRAP.OMP.EU'},
{'name': 'N.~Kochiashvili', 'affiliations': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia'], 'email': 'nino.kochiashvili@ILIAUNI.EDU.GE'},
{'name': 'A.~Kaeouach', 'affiliations': ['Observatory of Oukaimden,  Morocco'], 'email': 'aziz5200@live.com'},
{'name': 'J.-P.~Kneib', 'affiliations': ['Laboratoire d’astrophysique (LASTRO), Ecole Polytechnique Fed ́erale de Lausanne (EPFL), Observatoire de Sauverny, CH-1290 Versoix, Switzerland'], 'email': ''},
{'name': 'W.~Kou', 'affiliations': ['Beijing Planetarium, Beijing Academy of Science and Technology, Beijing, 100044, People’s Republic of China'], 'email': ''},
{'name': 'K.~Kruiswijk', 'affiliations': ['Centre for Cosmology, Particle Physics and Phenomenology - CP3, Universite Catholique de Louvain, B-1348 Louvain-la-Neuve, Belgium'], 'email': 'karlijn.kruiswijk@UCLOUVAIN.BE'},
{'name': 'S.~Lombardo', 'affiliations': ['Aix Marseille Univ, CNRS, CNES, LAM, Marseille, France'], 'email': 'simona.lombardo@LAM.FR'},
{'name': 'M.~Lamoureux', 'affiliations': ["Centre for Cosmology, Particle Physics and Phenomenology - CP3, Universit\\'e catholique de Louvain, B-1348 Louvain-la-Neuve, Belgium"], 'email': 'mathieu.lamoureux@uclouvain.be'},
{'name': 'N.~Leroy', 'affiliations': ['IJCLab, Univ Paris-Saclay, CNRS/IN2P3, Orsay, France'], 'email': 'leroy@LAL.IN2P3.FR'},
{'name': 'A.~Le~Van~Su', 'affiliations': ["OHP, Observatoire de Haute-Provence, CNRS, Aix Marseille University, Institut Pyth\\'eas, St Michel l’Observatoire, France"], 'email': ''},
{'name': 'J.~Mao', 'affiliations': ['Yunnan Observatories, Chinese Academy of Sciences, Kunming 650011, Yunnan Province, People’s Republic of China'], 'email': ''},
{'name': 'M.~Ma\\v{s},ek', 'affiliations': ['FZU - Institute of Physics of the Czech Academy of Sciences, Na Slovance 1999/2, CZ-182 21, Praha, Czech Republic'], 'email': 'masekma@FZU.CZ'},
{'name': 'T.~Midavaine', 'affiliations': ["Universit\\'e de Paris, CNRS, Astroparticule et Cosmologie, F-75013 Paris, France"], 'email': 'thierry.midavaine@INSTITUTOPTIQUE.FR'},
{'name': 'A.~M\\"{o}ller', 'affiliations': ['Centre for Astrophysics and Supercomputing, Swinburne University of Technology, Mail Number H29, PO Box 218, 31122 Hawthorn, VIC, Australia', 'ARC Centre of Excellence for Gravitational Wave Discovery (OzGrav), Hawthorn VIC 3122, Australia'], 'email': ''},
{'name': 'D.~Morris', 'affiliations': ['University of the Virgin Islands, United States Virgin Islands 00802, USA'], 'email': 'dmorris@UVI.EDU'},
{'name': 'R.~Natsvlishvili', 'affiliations': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia'], 'email': 'rezonats@YAHOO.COM'},
{'name': 'F.~Navarete', 'affiliations': ["SOAR Telescope/NSF's NOIRLab, Avda Juan Cisternas 1500, 1700000, La Serena, Chile"], 'email': 'navarete@GMAIL.COM'},
{'name': 'S.~Nissanke', 'affiliations': ['GRAPPA, Anton Pannekoek Institute for Astronomy and Institute of High-Energy Physics, University of Amsterdam, Science Park 904,1098 XH Amsterdam, The Netherlands'], 'email': 's.m.nissanke@UVA.NL'},
{'name': 'K.~Noonan', 'affiliations': ['University of the Virgin Islands, United States Virgin Islands 00802, USA'], 'email': 'kyle.noonan86@gmail.com'},
{'name': 'K.~Noysena', 'affiliations': ['National Astronomical Research Institute of Thailand (Public Organization), 260, Moo 4, T. Donkaew, A. Mae Rim, Chiang Mai, 50180, Thailand'], 'email': 'kanthanakorn@NARIT.OR.TH'},
{'name': 'N.~B.~Orange', 'affiliations': ['OrangeWave Innovative Science, LLC, Moncks Corner, SC 29461, USA'], 'email': 'orangewaveno@GMAIL.COM'},
{'name': 'J.~Peloton', 'affiliations': ['IJCLab, Univ Paris-Saclay, CNRS/IN2P3, Orsay, France'], 'email': 'peloton@LAL.IN2P3.FR'},
{'name': 'M.~Pilloix', 'affiliations': ["Artemis, Observatoire de la C\\^ote d’Azur, Universit\\'e C\\^ote d’Azur, Boulevard de l'Observatoire, 06304 Nice, France"], 'email': ''},
{'name': 'T.~Pradier', 'affiliations': ["Universit\\'e de Strasbourg, CNRS, IPHC UMR 7178, F-67000 Strasbourg, France"], 'email': 'thierry.pradier@IPHC.CNRS.FR'},
{'name': 'M.~Prouza', 'affiliations': ['FZU - Institute of Physics of the Czech Academy of Sciences, Na Slovance 1999/2, CZ-182 21, Praha, Czech Republic'], 'email': 'prouza@FZU.CZ'},
{'name': 'G.~Raaijmakers', 'affiliations': ['GRAPPA, Anton Pannekoek Institute for Astronomy and Institute of High-Energy Physics, University of Amsterdam, Science Park 904,1098 XH Amsterdam, The Netherlands'], 'email': 'g.raaijmakers@UVA.NL'},
{'name': 'Y.~Rajabov', 'affiliations': ['Ulugh Beg Astronomical Institute, Uzbekistan Academy of Sciences, Astronomy str. 33, Tashkent 100052, Uzbekistan'], 'email': 'rajabov@ASTRIN.UZ'},
{'name': 'J.-P.~Rivet', 'affiliations': ['Laboratoire J.-L. Lagrange, Universit de Nice Sophia-Antipolis, CNRS, Observatoire de la Cote d’Azur, F-06304 Nice, France'], 'email': ''},
{'name': 'Y.~Romanyuk', 'affiliations': ['Main Astronomical Observatory of National Academy of Sciences of Ukraine, 27 Acad. Zabolotnoho Str., Kyiv, 03143, Ukraine'], 'email': ''},
{'name': 'L.~Rousselot', 'affiliations': ["Soci\\'et\\'e Astronomique Populaire du Centre ,40 grande rue, 18340 Arçay, France"], 'email': ''},
{'name': 'F.~R\\"unger', 'affiliations': ['Institut f\\"ur Physik und Astronomie, Universit\\"at Potsdam, Karl-Liebknecht-Str. 24/25, D-14476 Potsdam, Germany'], 'email': ''},
{'name': 'V.~Rupchandani', 'affiliations': ['American University of Sharjah, Physics Department, PO Box 26666, Sharjah, UAE', 'Brown University, Providence, RI 02912, United States'], 'email': 'g00089000@AUS.EDU'},
{'name': 'T.~Sadibekova', 'affiliations': ['Ulugh Beg Astronomical Institute, Uzbekistan Academy of Sciences, Astronomy str. 33, Tashkent 100052, Uzbekistan', "Universit\\'e Paris-Saclay,\xa0Universit\\'e Paris Cit\\'e, CEA, CNRS, AIM, 91191, Gif-sur-Yvette, France"], 'email': 'tatyana.sadibekova@CEA.FR'},
{'name': 'N.~Sasaki', 'affiliations': ["Laborat\\'orio Nacional de Astrofísica, R. dos Estados Unidos, 154 - Nações, Itajub\\'a - MG, 37504-364, Brazil"], 'email': ''},
{'name': 'A. Simon', 'affiliations': ['Astronomy and Space Physics Department, Taras Shevchenko National University of Kyiv, Glushkova ave., 4, Kyiv, 03022, Ukraine', 'National Center Junior academy of sciences of Ukraine, 38-44, Dehtiarivska St., Kyiv, 04119, Ukraine'], 'email': 'skazhenijandrew@GMAIL.COM'},
{'name': 'K.~Smith', 'affiliations': ['University of the Virgin Islands, United States Virgin Islands 00802, USA'], 'email': 'kiwanee90@gmail.com'},
{'name': 'O.~Sokoliuk', 'affiliations': ['Astronomical Observatory\\ Taras Shevshenko National University of Kyiv, Observatorna str. 3, Kyiv, 04053, Ukraine', 'Main Astronomical Observatory of National Academy of Sciences of Ukraine, 27 Acad. Zabolotnoho Str., Kyiv, 03143, Ukraine'], 'email': ''},
{'name': 'X.~Song', 'affiliations': ['Beijing Planetarium, Beijing Academy of Science and Technology, Beijing, 100044, People’s Republic of China'], 'email': 'famc2@163.COM'},
{'name': 'A.~Takey', 'affiliations': ['National Research Institute of Astronomy and Geophysics, 1 El-marsad St., Helwan, Cairo, Egypt'], 'email': ''},
{'name': 'Y.~Tillayev', 'affiliations': ['Ulugh Beg Astronomical Institute, Uzbekistan Academy of Sciences, Astronomy str. 33, Tashkent 100052, Uzbekistan', 'National University of Uzbekistan, 4 University str., Tashkent 100174, Uzbekistan'], 'email': 'yusuf@ASTRIN.UZ'},
{'name': 'I.~Tosta~e~Melo', 'affiliations': ['INFN, Laboratori Nazionali del Sud, I-95125 Catania, Italy'], 'email': 'itostaemelo@UNISS.IT'},
{'name': 'D.~Turpin', 'affiliations': ["Universit\\'e Paris-Saclay, Universit\\'e Paris Cit\\'e, CEA, CNRS, AIM, 91191, Gif-sur-Yvette, France"], 'email': 'damien.turpin@CEA.FR'},
{'name': 'A.~de~Ugarte~Postigo', 'affiliations': ["Artemis, Observatoire de la C\\^ote d’Azur, Universit\\'e C\\^ote d’Azur, Boulevard de l'Observatoire, 06304 Nice, France"], 'email': 'adeugartepostigo@GMAIL.COM'},
{'name': 'M.~Vardosanidze', 'affiliations': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia', 'Samtskhe-Javakheti  State  University, Rustaveli Str. 113,  Akhaltsikhe, 0080,  Georgia'], 'email': 'manana.vardosanidze.1@ILIAUNI.EDU.GE'},
{'name': 'X.~F.~Wang', 'affiliations': ['Beijing Planetarium, Beijing Academy of Science and Technology, Beijing, 100044, People’s Republic of China', 'Physics Department and Astronomy Department, Tsinghua University, Beijing, 100084, People’s Republic of China'], 'email': 'wang_xf@MAIL.TSINGHUA.EDU.CN'},
{'name': 'D.~Vernet', 'affiliations': ["Observatoire de la C\\^ote d'Azur, CNRS, UMS Galil\\'ee, France"], 'email': ''},
{'name': 'Z.~Vidadi', 'affiliations': ['N.Tusi Shamakhy Astrophysical Observatory Azerbaijan National Academy of Sciences, settl.Y. Mammadaliyev, AZ 5626, Shamakhy, Azerbaijan'], 'email': 'zumrudvidadiqizi@GMAIL.COM'},
{'name': 'J.~Zhu', 'affiliations': ['Beijing Planetarium, Beijing Academy of Science and Technology, Beijing, 100044, People’s Republic of China'], 'email': 'jinzhu@BJP.ORG.CN'},
{'name': 'Y.~Zhu', 'affiliations': ['Key Laboratory of Optical Astronomy, National Astronomical Observatories, Chinese Academy of Sciences, A20, Datun Road, Chaoyang District, Beijing 100012, People’s Republic of China'], 'email': 'bjtwg@139.COM'}
]

institution_list_ordered = []
for author in authors:
    institutions = author["affiliations"]
    for institution in institutions:
        if institution in institution_list_ordered: continue
        institution_list_ordered.append(institution)

print('--------')
print(f"Total {len(authors)} authors") 

nature_style = False
spie_style = True

if nature_style:
    author_list = []

    for author in authors:
        author_institutions = author["affiliations"]
        indices = []
        for author_institution in author_institutions:
            indices.append(institution_list_ordered.index(author_institution))
        author_list.append('%s$^{%s}$' % (author["name"], ",".join([str(x+1) for x in indices])))


    
    print(", ".join(author_list))
    
    institution_list = []
    for ii, institution in enumerate(institution_list_ordered):
        institution_list.append('$^{%s}$ %s' % (str(ii+1), institution))
    print("\n".join(institution_list)) 
    
    print("--------")
    institution_list = []
    for ii, institution in enumerate(institution_list_ordered):
        institution_list.append('\item %s' % (institution))
    print("\n".join(institution_list))
    
if spie_style:
    author_list = []
    for author in authors:
        author_institutions = author["affiliations"]
        indices = []
        for author_institution in author_institutions:
            indices.append(institution_list_ordered.index(author_institution))
        author_list.append('\\author[%s]{%s}' % (",".join([str(x+1) for x in indices]), author["name"]))

    print("\n".join(author_list))

    institution_list = []
    for ii, institution in enumerate(institution_list_ordered):
        institution_list.append('\\affil[%s]{%s}' % (str(ii+1), institution))
    print("\n".join(institution_list))

fieldnames = ["name", "email", "affiliations"]
with open('authors.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerows(authors)
