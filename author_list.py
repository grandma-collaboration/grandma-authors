# Author: Michael Coughlin :)
import csv
import os
import numpy as np
import sys

authors = [
{'name': 'I.~Tosta~e~Melo', 'affiliations': ['Department of Physics and Astronomy, University of Catania, 95125 Catania, Italy'], 'email': 'iara.tosta.melo@dfa.unict.it'},
{'name': 'J.-G.~Ducoin', 'affiliations': ["Institut d'Astrophysique de Paris, 98 bis boulevard Arago, 75014 Paris, France"], 'email': 'ducoin@IAP.FR'},
{'name': 'Z.~Vidadi', 'affiliations': ['N.Tusi Shamakhy Astrophysical Observatory Azerbaijan National Academy of Sciences, settl.Y. Mammadaliyev, AZ 5626, Shamakhy, Azerbaijan'], 'email': 'zumrudvidadiqizi@GMAIL.COM', 'orcid': '0009-0002-3591-0568'},
{'name': 'C.~Andrade', 'affiliations': ['School of Physics and Astronomy, University of Minnesota, Minneapolis, Minnesota 55455, USA'], 'email': 'andra104@UMN.EDU', 'orcid': '0009-0004-9687-3275'},
{'name': 'V.~Rupchandani', 'affiliations': ['Brown University, Providence, RI 02912, Rhode Island, USA'], 'email': ''},
{'name': 'J.~Abdelhadi', 'affiliations': ["Oukaimeden Observatory,High Energy Physics and Astrophysics Laboratory, FSSM, Cadi Ayyad University  Av. Prince My Abdellah, BP 2390 Marrakesh, Morocco"], 'email': ''},
{'name': 'L. ~Abe', 'affiliations': 'Lagrange-OCA'], 'email': ''},
{'name': 'S.~Agayeva', 'affiliations': ['N.Tusi Shamakhy Astrophysical Observatory Azerbaijan National Academy of Sciences, settl.Y. Mammadaliyev, AZ 5626, Shamakhy, Azerbaijan'], 'email': 'sebnem-agayeva-94@MAIL.RU', 'orcid': '0009-0007-3673-8997'},
{'name': 'O.~Aguerre-Chariol', 'affiliations': ['14 rue Saint-Hubert, F-60560 Orry-la-Ville, France'], 'email': 'oaguerre@club-internet.fr', 'orcid' : '0000-0001-9488-9530'},
{'name': 'V.~Aivazyan', 'affiliations': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia', 'Samtskhe-Javakheti  State  University, Rustaveli Str. 113,  Akhaltsikhe, 0080,  Georgia'], 'email': 'vovaaivazian10@GMAIL.COM'},
{'name': 'S.~Alishov', 'affiliations': ['N.Tusi Shamakhy astrophysical Observatory Azerbaijan National Academy of Sciences, settl.Mamedaliyev, AZ 5626, Shamakhy, Azerbaijan'], 'email': 'sebaheddin.ali@GMAIL.COM'},
{'name': 'S.~Antier', 'affiliations': ["Artemis, Observatoire de la C\\^ote d'Azur, Universit\\'e C\\^ote d'Azur, Boulevard de l'Observatoire, 06304 Nice, France"], 'email': 'sarah.antier@OCA.EU', 'orcid': '0000-0002-7686-3334'},
{'name': 'J.-M.~Bai', 'affiliations': ["YNAO"], 'email': ''},
{'name': 'A.~Baransky', 'affiliations': ['Astronomical Observatory Taras Shevshenko National University of Kyiv, Observatorna str. 3, Kyiv, 04053, Ukraine'], 'email': 'abaransky@UKR.NET', 'orcid': '0000-0002-9808-1990'},
{'name': 'S.~Bednarz', 'affiliations': ['Silesian University of Technology, Faculty of Automatic Control, Electronics and Computer Science, Akademicka 16, 44-100 Gliwice, Poland'], 'email': 'sbendarz@polsl.pl', 'orcid' : '0000-0002-2764-7328'},
{'name': 'Ph.~Bendjoya', 'affiliations': 'Lagrange-OCA'], 'email': ''},
{'name': 'Z.~Benkhaldoun', 'affiliations': ["Oukaimeden Observatory,High Energy Physics and Astrophysics Laboratory, FSSM, Cadi Ayyad University  Av. Prince My Abdellah, BP 2390 Marrakesh, Morocco"], 'email': 'zouhair@uca.ac.ma', 'orcid': '0000-0001-6285-9847',},
{'name': 'S.~Beradze', 'affiliations': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia', 'Samtskhe-Javakheti  State  University, Rustaveli Str. 113,  Akhaltsikhe, 0080,  Georgia'], 'email': 'beradze.sophia@GMAIL.COM', 'orcid': '0000-0002-8291-2817'},
{'name': 'U.~Bhardwaj', 'affiliations': ['GRAPPA, Anton Pannekoek Institute for Astronomy and Institute of High-Energy Physics, University of Amsterdam, Science Park 904,1098 XH Amsterdam, The Netherlands'], 'email': 'u.bhardwaj@UVA.NL'},
{'name': 'M.~Blazek', 'affiliations': ['FZU - Institute of Physics of the Czech Academy of Sciences, Na Slovance 1999/2, CZ-182 21, Praha, Czech Republic'], 'email': 'embee.cz@GMAIL.COM'},
{'name': 'M.~Bo\\"er', 'affiliations': ["Artemis, Observatoire de la C\\^ote d'Azur, Universit\\'e C\\^ote d'Azur, Boulevard de l'Observatoire, 06304 Nice, France"], 'email': 'michel.boer@oca.eu', 'orcid': '0000-0001-9157-4349'},
{'name': 'E.~Broens', 'affiliations': ['Vereniging Voor Sterrenkunde, Balen-Neetlaan 18A, 2400, Mol, Belgium'], 'email': 'eric.broens@skynet.be', 'orcid': '0000-0003-1523-4478'},
{'name': 'O.~Burkhonov', 'affiliations': ['Ulugh Beg Astronomical Institute, Uzbekistan Academy of Sciences, Astronomy str. 33, Tashkent 100052, Uzbekistan'], 'email': 'boa@ASTRIN.UZ', 'orcid': '0000-0003-1169-6763'},
{'name': 'W.~Corradi', 'affiliations': ["Laborat\\'orio Nacional de Astrof\\'isica, R. dos Estados Unidos, 154 - Na\\c{c}\\~oes, Itajub\\'a - MG, 37504-364, Brazil"], 'email': 'wbcorradi@LNA.BR'},
{'name': 'M.~W.~Coughlin', 'affiliations': ['School of Physics and Astronomy, University of Minnesota, Minneapolis, Minnesota 55455, USA'], 'email': 'cough052@umn.edu', 'orcid': '0000-0002-8262-2924'},
{'name': 'T.~Culino', 'affiliations': ["Artemis, Observatoire de la C\\^ote d'Azur, Universit\\'e C\\^ote d'Azur, Boulevard de l'Observatoire, 06304 Nice, France"], 'email': 'thomas.culino@EDU.DEVINCI.FR'},
{'name': 'D.~Datashvili', 'affiliations': ["E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia', 'Samtskhe-Javakheti  State  University, Rustaveli Str. 113,  Akhaltsikhe, 0080,  Georgia"], 'email': ''}   
{'name': 'D.~Dornic', 'affiliations': ['CPPM, Aix Marseille Univ, CNRS/IN2P3, CPPM, Marseille, France'], 'email': 'dornic@CPPM.IN2P3.FR', 'orcid': '0000-0001-5729-1468'},
{'name': 'P.-A.~Duverne', 'affiliations': ["Universit\\'e Paris Cit\\'e, CNRS, Astroparticule et Cosmologie, F-75013 Paris, France"], 'email': 'pierre-alexandre.duverne@U-PSUD.FR'},
{'name': 'A.~Eid', 'affiliations': 'The National Research Institute of Astronomy and Geophysics (NRIAG)'], 'email': ''},
{'name': 'E.~Elhosseiny', 'affiliations': ["National Research Institute of Astronomy and Geophysics (NRIAG), 1 El-marsad St., 11421 Helwan, Cairo, Egypt"], 'email': 'eslam_elhosseiny@nriag.sci.eg', 'orcid': '0000-0002-9751-8089'},
{'name': 'L.~Eymar', 'affiliations': [" "], 'email': ''},
{'name': 'M.~Farouk', 'affiliations': 'The National Research Institute of Astronomy and Geophysics (NRIAG)'. ], 'email': ''},
{'name': 'A.~Fouad', 'affiliations': ['National Research Institute of Astronomy and Geophysics (NRIAG), 1 El-marsad St., 11421 Helwan, Cairo, Egypt'], 'email': 'ahmed.fouad@nriag.sci.eg'},
{'name': 'M.~Freeberg', 'affiliations': ['KNC, AAVSO, Hidden Valley Observatory(HVO), Colfax, WI.; iTelescope, NMS, Mayhill, NM.'], 'email': 'mdfreeb@gmail.com', 'orcid' : '0009-0005-4287-7198'},
{'name': 'F.~Guo', 'affiliations': ["Physics Department and Astronomy Department, Tsinghua University, Beijing, 100084, People's Republic of China"], 'email': 'gfz20@MAILS.TSINGUA.EDU.CN'},
{'name': 'P.~Gokuldass', 'affiliations': ['Department of Aerospace, Physics, and Space Sciences, Florida Institute of Technology, Melbourne, Florida 32901, USA'], 'email': 'priyadass.94@GMAIL.COM'},
{'name': 'N.~Guessoum', 'affiliations': ['American University of Sharjah, Physics Department, PO Box 26666, Sharjah, UAE'], 'email': 'nguessoum@AUS.EDU'},
{'name': 'E.~Gurbanov', 'affiliations': ['N.Tusi Shamakhy Astrophysical Observatory Azerbaijan National Academy of Sciences, settl.Y. Mammadaliyev, AZ 5626, Shamakhy, Azerbaijan'], 'email': 'emingurban88@GMAIL.COM'},
{'name': 'R.~Hainich', 'affiliations': ['Institut f\\"ur Physik und Astronomie, Universit\\"at Potsdam, Karl-Liebknecht-Str. 24/25, D-14476 Potsdam, Germany'], 'email': 'rhainich@ASTRO.PHYSIK.UNI-POTSDAM.DE'},
{'name': 'G.~M. Hamed', 'affiliations': ['Department of Astronomy, National Research Institute of Astronomy and Geophysics, 11421 Helwan , Cairo, Egypt'], 'email': 'gamal.hamed@nriag.sci.eg'},
{'name': 'E.~Hasanov', 'affiliations': ['N.Tusi Shamakhy Astrophysical Observatory Azerbaijan National Academy of Sciences, settl.Y. Mammadaliyev, AZ 5626, Shamakhy, Azerbaijan'], 'email': 'emrah.hesenov.2020@GMAIL.COM'},
{'name': 'P.~Hello', 'affiliations': ['IJCLab, Univ Paris-Saclay, CNRS/IN2P3, Orsay, France'], 'email': 'patrice.hello@IJCLAB.IN2P3.FR'},
{'name': 'R.~Inasaridze', 'affiliations': ["E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia', 'Samtskhe-Javakheti  State  University, Rustaveli Str. 113,  Akhaltsikhe, 0080,  Georgia"], 'email': ''},
{'name': 'A.~Iskandar', 'affiliations': ["Xinjiang Astronomical Observatory, Chinese Academy of Sciences, Urumqi, Xinjiang 830011, People's Republic of China", "School of Astronomy and Space Science, University of Chinese Academy of Sciences, Beijing 100049, People's Republic of China"], 'email': 'abudu@xao.ac.cn'},
{'name': 'N.~Ismailov', 'affiliations': ['N.Tusi Shamakhy Astrophysical Observatory Azerbaijan National Academy of Sciences, settl.Y. Mammadaliyev, AZ 5626, Shamakhy, Azerbaijan'], 'email': 'ismailovnshao@GMAIL.COM', 'orcid': '0000-0002-5307-4295'},
{'name': 'A.~Janati', 'affiliations': ["Oukaimeden Observatory, HAO Telescope"], 'email': ''},
{'name': 'T.~Jegou~du~Laz', 'affiliations': ['Division of Physics, Mathematics, and Astronomy, California Institute of Technology, Pasadena, CA 91125, USA'], 'email': 'tdulaz@caltech.edu', 'orcid': '0009-0003-6181-4526'},
{'name': 'D.~A.~Kann', 'affiliations': ["Hessian Research Cluster ELEMENTS, Giersch Science Center, Max-von-Laue-Stra{\\ss}e 12, Goethe University Frankfurt, Campus Riedberg, 60438 Frankfurt am Main, Germany"], 'email': 'ultralonggrbsn@gmail.com', 'orcid': '0000-0003-2902-3583'},
{'name': 'G.~Kapanadze', 'affiliations': ["E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia', 'Samtskhe-Javakheti  State  University, Rustaveli Str. 113,  Akhaltsikhe, 0080,  Georgia"], 'email': ''},   
{'name': 'R.~W.~Kiendrebeogo', 'affiliations': [ "Laboratoire de Physique et de Chimie de l'Environnement, Universit\\'e Joseph KI-ZERBO, Ouagadougou, Burkina Faso", "Artemis, Observatoire de la C\\^ote d'Azur, Universit\\'e C\\^ote d'Azur, Boulevard de l'Observatoire, 06304 Nice, France",  "School of Physics and Astronomy, University of Minnesota, Minneapolis, Minnesota 55455, USA"], 'email': 'weizmann.kiendrebeogo@OCA.EU', 'orcid': '0000-0002-9108-5059'},
{'name': 'A.~Klotz', 'affiliations': ["IRAP, Universit\\'e de Toulouse, CNRS, UPS, 14 Avenue Edouard Belin, F-31400 Toulouse, France", "Universit\\'e Paul Sabatier Toulouse III, Universit'e de Toulouse, 118 route de Narbonne, 31400 Toulouse, France"], 'email': 'aklotz@IRAP.OMP.EU', 'orcid': '0000-0002-2652-0069'},
{'name': 'R.~Kneip', 'affiliations': ['K26 / Contern Observatory (private obs.), 1, beim Schmilberbour, 5316 Contern, Luxembourg'], 'email': 'raymond.kneip@education.lu'},
{'name': 'N.~Kochiashvili', 'affiliations': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia'], 'email': 'nino.kochiashvili@ILIAUNI.EDU.GE'}, 
{'name': 'A.~Kaeouach', 'affiliations': ['Oukaimeden Observatory (HAO), Oukaimeden,  Morocco'], 'email': 'aziz5200@live.com', 'orcid': '0000-0001-5249-4354'},
{'name': 'K.~Kruiswijk', 'affiliations': ['Centre for Cosmology, Particle Physics and Phenomenology - CP3, Universite Catholique de Louvain, B-1348 Louvain-la-Neuve, Belgium'], 'email': 'karlijn.kruiswijk@UCLOUVAIN.BE'},
{'name': 'N.~Leroy', 'affiliations': ['IJCLab, Univ Paris-Saclay, CNRS/IN2P3, Orsay, France'], 'email': 'leroy@LAL.IN2P3.FR'},
{'name': 'J.~Mao', 'affiliations': ["Yunnan Observatories, Chinese Academy of Sciences, Kunming 650011, Yunnan Province, People's Republic of China"], 'email': ''},
{'name': 'D.~Marchais', 'affiliations': ['Observatoire du Crous des Gats, F-31550 Cintegabelle, France'], 'email': 'denis.marchais@free.fr', 'orcid' : '0009-0004-2563-0399'},
{'name': 'M.~Ma\\v{s},ek', 'affiliations': ['FZU - Institute of Physics of the Czech Academy of Sciences, Na Slovance 1999/2, CZ-182 21, Praha, Czech Republic'], 'email': 'masekma@FZU.CZ'},
{'name': 'T.~Midavaine', 'affiliations': ["Soci\\'t\\' astronomique de France, 3 rue Beethoven, F-75016 Paris, France"], 'email': 'thierrymidavaine@sfr.fr'},
{'name': 'D.~Morris', 'affiliations': ["University of the Virgin Islands, United States Virgin Islands 00802, USA"], 'email': 'dmorris@uvi.edu'},
{'name': 'R.~Natsvlishvili', 'affiliations': ["E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia', 'Samtskhe-Javakheti  State  University, Rustaveli Str. 113,  Akhaltsikhe, 0080,  Georgia"], 'email': ''},
{'name': 'F.~Navarete', 'affiliations': ["SOAR Telescope/NSF's NOIRLab, Avda Juan Cisternas 1500, 1700000, La Serena, Chile"], 'email': 'navarete@GMAIL.COM'},
{'name': 'K.~Noonan', 'affiliations': ['University of the Virgin Islands, United States Virgin Islands 00802, USA'], 'email': 'kyle.noonan86@gmail.com'},
{'name': 'K.~Noysena', 'affiliations': ['National Astronomical Research Institute of Thailand (Public Organization), 260, Moo 4, T. Donkaew, A. Mae Rim, Chiang Mai, 50180, Thailand'], 'email': 'kanthanakorn@NARIT.OR.TH', 'orcid': '0000-0001-9109-8311',},
{'name': 'A.~Oksanen', 'affiliations': ['Hankasalmi Observatory, Jyvaskylan Sirius ry, Verkkoniementie 30, FI-40950 Muurame, Finland'], 'email': '', 'orcid' : '0000-0001-6249-6062'},
{'name': 'N.~B.~Orange', 'affiliations': ['OrangeWave Innovative Science, LLC, Moncks Corner, SC 29461, USA'], 'email': 'orangewaveno@GMAIL.COM', 'orcid': '0000-0002-7198-3476'},
{'name': 'M.~Pilloix', 'affiliation': ["Artemis, Observatoire de la Côte d’Azur, Université Côte d’Azur, Boulevard de l'Observatoire, 06304 Nice, France"]},
{'name': 'A.~Popowicz', 'affiliations': ['Silesian University of Technology, Department of Electronics, Electrical Engineering and Microelectronics, Akademicka 16, 44-100 Gliwice, Poland'], 'email': 'apopowicz@polsl.pl', 'orcid' : '0000-0003-3184-5228'},
{'name': 'T.~Pradier', 'affiliations': ["Universit\\'e de Strasbourg, CNRS, IPHC UMR 7178, F-67000 Strasbourg, France"], 'email': 'thierry.pradier@IPHC.CNRS.FR', 'orcid': '0000-0001-5501-0060'},
{'name': 'O.~Pyshna', 'affiliations': ['Astronomical Observatory of Taras Shevchenko National University of Kyiv, Observatorna Str. 3, Kyiv, 04053, Ukraine'], 'email': ''},
{'name': 'G. Raaijmakers', 'affiliations': ['GRAPPA, Anton Pannekoek Institute for Astronomy and Institute of High-Energy Physics, University of Amsterdam, Science Park 904,1098 XH Amsterdam, The Netherlands']},
{'name': 'Y.~Rajabov', 'affiliations': ['Ulugh Beg Astronomical Institute, Uzbekistan Academy of Sciences, Astronomy str. 33, Tashkent 100052, Uzbekistan'], 'email': 'rajabov@ASTRIN.UZ', 'orcid': '0000-0001-9878-9553'}, 
{'name': 'C.~Rinner', 'affiliations': ['Oukaimeden Observatory (MOSS), Oukaimeden,  Morocco'], 'email': 'claudine.rinner@laposte.net', 'orcid': '0000-0001-9878-9553'},
{'name': 'J.-P.~Rivet', 'affiliations': ["Laboratoire J.-L. Lagrange, Universit\\'e de Nice Sophia-Antipolis, CNRS, Observatoire de la Cote d'Azur, F-06304 Nice, France"], 'email': 'jean-pierre.rivet@oca.eu', 'orcid': '0000-0002-0289-5851'},
{'name': 'M.~Sabil', 'affiliations': ["Oukaimeden Observatory,High Energy Physics and Astrophysics Laboratory, FSSM, Cadi Ayyad University  Av. Prince My Abdellah, BP 2390 Marrakesh, Morocco"], 'email': ''},
{'name': 'T.~Sadibekova', 'affiliations': ['Ulugh Beg Astronomical Institute, Uzbekistan Academy of Sciences, Astronomy str. 33, Tashkent 100052, Uzbekistan', "Universit\\'e Paris-Saclay, Universit\\'e Paris Cit\\'e, CEA, CNRS, AIM, 91191, Gif-sur-Yvette, France"], 'email': 'tatyana.sadibekova@CEA.FR'},
{'name': 'N.~Sasaki', 'affiliations': ["Laborat\\'orio Nacional de Astrof\\'isica, R. dos Estados Unidos, 154 - Na\\c{c}\\~oes, Itajub\\'a - MG, 37504-364, Brazil"], 'email': 'nsasaki@lna.br '},
{'name': 'M.~Serrau','affiliations:'["Soci\\'et\\'e Astronomique de France, Observatoire de Dauban, FR 04150 Banon, France"],'email':'marc.serrau2@free.fr'},
{'name': 'A.~Simon', 'affiliations': ['Astronomy and Space Physics Department, Taras Shevchenko National University of Kyiv, Glushkova ave., 4, Kyiv, 03022, Ukraine', 'National Center Junior academy of sciences of Ukraine, 38-44, Dehtiarivska St., Kyiv, 04119, Ukraine'], 'email': 'skazhenijandrew@GMAIL.COM'},
{'name': 'A.~Shokry', 'affiliations': ['Astronomy Dept., National Research Institute of Astronomy and Geophysics, (NRIAG), Helwan, Cairo, Egypt'], 'email' : 'ahmedsh2911@gmail.com'},
{'name': 'K.~Smith', 'affiliations': ["University of the Virgin Islands, United States Virgin Islands 00802, USA"], 'email': 'kiwanee90@gmail.com'},
{'name': 'O.~Sokoliuk', 'affiliations': ['Astronomical Observatory\\ Taras Shevshenko National University of Kyiv, Observatorna str. 3, Kyiv, 04053, Ukraine', 'Main Astronomical Observatory of National Academy of Sciences of Ukraine, 27 Acad. Zabolotnoho Str., Kyiv, 03143, Ukraine'], 'email': ''},
{'name': 'X.~Song', 'affiliations': ["Beijing Planetarium, Beijing Academy of Science and Technology, Beijing, 100044, People's Republic of China"], 'email': 'famc2@163.COM'},
{'name': 'A.~Takey', 'affiliations': ['National Research Institute of Astronomy and Geophysics (NRIAG), 1 El-marsad St., 11421 Helwan, Cairo, Egypt'], 'email': 'ali.takey@nriag.sci.eg', 'orcid': '0000-0003-1423-5516'},
{'name': 'P.~Thierry', 'affiliations': ["CNRS-OMP-IRAP"], 'email': ''},
{'name': 'Y.~Tillayev', 'affiliations': ['Ulugh Beg Astronomical Institute, Uzbekistan Academy of Sciences, Astronomy str. 33, Tashkent 100052, Uzbekistan', 'National University of Uzbekistan, 4 University str., Tashkent 100174, Uzbekistan'], 'email': 'yusuf@ASTRIN.UZ', 'orcid': '0000-0002-2861-1343'},
{'name': 'D.~Turpin', 'affiliations': ["Universit\\'e Paris-Saclay, Universit\\'e Paris Cit\\'e, CEA, CNRS, AIM, 91191, Gif-sur-Yvette, France"], 'email': 'damien.turpin@CEA.FR', 'orcid': '0000-0003-1835-1522'},
{'name': 'A.~de~Ugarte~Postigo', 'affiliations': ["Artemis, Observatoire de la C\\^ote d'Azur, Universit\\'e C\\^ote d'Azur, Boulevard de l'Observatoire, 06304 Nice, France"], 'email': 'adeugartepostigo@GMAIL.COM', 'orcid': '0000-0001-7717-5085'},
{'name': 'M.~Vardosanidze', 'affiliations': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia', 'Samtskhe-Javakheti  State  University, Rustaveli Str. 113,  Akhaltsikhe, 0080,  Georgia'], 'email': 'manana.vardosanidze.1@ILIAUNI.EDU.GE'}, 
{'name': 'V.~Vasylenko', 'affiliations': ["Astronomy and Space Physics Department, Taras Shevchenko National University of Kyiv, Glushkova Ave., 4, Kyiv, 03022, Ukraine", "National Center Junior Academy of Sciences of Ukraine, Dehtiarivska St. 38-44, Kyiv, 04119, Ukraine"], 'email': ''},
{'name': 'D.~Vernet', 'affiliations': 'Galilee-OCA']},
{'name': 'L.~Wang', 'affiliations': ['Xinjiang Astronomical Observatory, 150 Science 1-Street, Urumqi, Xinjiang 830011, China'], 'email': 'wangletian@xao.ac.cn'},
{'name': 'F.~Vachier ', 'affiliations': ["CNRS-OMP-IRAP"], 'email': ''},
{'name': 'J.~P.~Vignes', 'affiliations': ['KNC Deep Sky Chile Observatory'], 'email': ''},
{'name': 'X.~F.~Wang', 'affiliations': ["Beijing Planetarium, Beijing Academy of Science and Technology, Beijing, 100044, People's Republic of China', 'Physics Department and Astronomy Department, Tsinghua University, Beijing, 100084, People's Republic of China"], 'email': 'wang_xf@MAIL.TSINGHUA.EDU.CN'},
{'name': 'X. ~Zeng', 'affiliations': ['Xinjiang Astronomical Observatory, 150 Science 1-Street, Urumqi, Xinjiang 830011, China'], 'email': 'xyzeng2018@163.com'},
{'name': 'J.~Zhang', 'affiliations': ["Key Laboratory of Optical Astronomy, National Astronomical Observatories, Chinese Academy of Sciences, A20, Datun Road, Chaoyang District, Beijing 100012, People's Republic of China"], 'email': ''},
{'name': 'Y.~Zhu', 'affiliations': ["Key Laboratory of Optical Astronomy, National Astronomical Observatories, Chinese Academy of Sciences, A20, Datun Road, Chaoyang District, Beijing 100012, People's Republic of China"], 'email': 'bjtwg@139.COM'},

]

institution_list_ordered = []
for author in authors:
    institutions = author["affiliations"]
    for institution in institutions:
        if institution in institution_list_ordered: continue
        institution_list_ordered.append(institution)

print('--------')
print(f"Total {len(authors)} authors") 

mnras_style = True
nature_style = False
spie_style = False

if mnras_style:
    author_list = []

    for ii, author in enumerate(authors):
        author_institutions = author["affiliations"]
        indices = []
        for author_institution in author_institutions:
            indices.append(institution_list_ordered.index(author_institution))
        author_list.append('%s$^{%s}$' % (author["name"], ",".join([str(x+1) for x in indices])))
        if np.mod(ii, 4) == 0 and ii > 0:
            author_list.append('\\newauthor')


    print(", ".join(author_list))

    institution_list = []
    for ii, institution in enumerate(institution_list_ordered):
        institution_list.append('$^{%s}$ %s' % (str(ii+1), institution))
    print("\\\\ \n".join(institution_list))

    print("--------")
    institution_list = []
    for ii, institution in enumerate(institution_list_ordered):
        institution_list.append('\item %s' % (institution))
    print("\n".join(institution_list))

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

fieldnames = ["name", "email", "affiliations", "orcid"]
with open('authors.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerows(authors)
