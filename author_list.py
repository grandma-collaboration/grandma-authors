# Author: Michael Coughlin
import os
import sys

authors = {'S. Agayeva': ['N.Tusi Shamakhy astrophysical Observatory Azerbaijan National Academy of Sciences, settl.Mamedaliyev, AZ 5626, Shamakhy, Azerbaijan'],
           'V. Aivazyan': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia', 'Samtskhe-Javakheti  State  University, Rustaveli Str. 113,  Akhaltsikhe, 0080,  Georgia'],
           'S. Alishov': ['N.Tusi Shamakhy astrophysical Observatory Azerbaijan National Academy of Sciences, settl.Mamedaliyev, AZ 5626, Shamakhy, Azerbaijan'], 
           'M. Almualla': ['American University of Sharjah, Physics Department, PO Box 26666, Sharjah, UAE'],
           'C. Andrade': ["School of Physics and Astronomy, University of Minnesota, Minneapolis, Minnesota 55455, USA"],
           'S. Antier': ["Artemis, Observatoire de la Côte d’Azur, Université Côte d’Azur, Boulevard de l'Observatoire, 06304 Nice, France"], 
           'J.-M. Bai': ['Yunnan Observatories, Chinese Academy of Sciences, Kunming 650011, Yunnan, People’s Republic of China'],
           'A. Baransky': ["Astronomical Observatory Taras Shevshenko National University of Kyiv, Observatorna str. 3, Kyiv, 04053, Ukraine"],
           'S. Basa': ["Aix Marseille Univ, CNRS, CNES, LAM, IPhU, Marseille, France"],
           'P. Bendjoya': ['Laboratoire J.-L. Lagrange, Universit de Nice Sophia-Antipolis, CNRS, Observatoire de la Cote d’Azur, F-06304 Nice, France'],
           'Z. Benkhaldoun': ["Universit ́e Cadi Ayyad, Facult ́e des Sciences Semlalia, Av. Prince My Abdellah, BP 2390 Marrakesh, Morocco"],
           'S. Beradze': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia', 'Samtskhe-Javakheti  State  University, Rustaveli Str. 113,  Akhaltsikhe, 0080,  Georgia'],
           'D. Berezin': ['ICAMER Observatory of NAS of Ukraine 27 Acad. Zabolotnoho Str., Kyiv, 03143, Ukraine'],
           'U. Bhardwaj': ["GRAPPA, Anton Pannekoek Institute for Astronomy and Institute of High-Energy Physics, University of Amsterdam, Science Park 904,1098 XH Amsterdam, The Netherlands"],
           'M.-A. Bizouard': ["Artemis, Observatoire de la Côte d’Azur, Université Côte d’Azur, Boulevard de l'Observatoire, 06304 Nice, France"],
           'M. Blazek': ["Instituto de Astrof\\'isica de Andaluc\\'ia (IAA-CSIC), Glorieta de la Astronom\\'ia s/n, 18008 Granada, Spain"],
           'O. Burkhonov': ['Ulugh Beg Astronomical Institute, Uzbekistan Academy of Sciences, Astronomy str. 33, Tashkent 100052, Uzbekistan'],
           'E. Burns': ['Department of Physics \\& Astronomy, Louisiana State University, Baton Rouge, LA 70803, USA'],
           'S. Caudill': ['Institute for Gravitational and Subatomic Physics (GRASP), Utrecht University, Princetonplein 1, 3584 CC, Utrecht, The Netherlands', 'Nikhef, Science Park 105, 1098 XG, Amsterdam, The Netherlands'],
           'N. Christensen': ["Artemis, Observatoire de la Côte d’Azur, Université Côte d’Azur, Boulevard de l'Observatoire, 06304 Nice, France"],
           'F. Colas': ["Astronomie et Systèmes Dynamiques, Institut de Mécanique Céleste et de Calcul des Éphémérides CNRS UMR 8028, Observatoire de Paris, Université PSL, Sorbonne Université, 77 Avenue Denfert-Rochereau, 75014 Paris, France"],
           'A. Coleiro': ["Universit\\'e de Paris, CNRS, Astroparticule et Cosmologie, F-75013 Paris, France"],
           'W. Corradi': ["Laboratório Nacional de Astrofísica, R. dos Estados Unidos, 154 - Nações, Itajubá - MG, 37504-364, Brazil"],
           'M. W. Coughlin': ["School of Physics and Astronomy, University of Minnesota, Minneapolis, Minnesota 55455, USA"],
           'T. Culino': ["Artemis, Observatoire de la Côte d’Azur, Université Côte d’Azur, Boulevard de l'Observatoire, 06304 Nice, France"],
           'D. Darson': ["Ecole Normale Sup ́erieure, CNRS-PSL, Research University, 45, rue d’Ulm 75230 Paris Cedex 5 France"],
           'D. Datashvili': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia', 'Samtskhe-Javakheti  State  University, Rustaveli Str. 113,  Akhaltsikhe, 0080,  Georgia'],
           'T. Dietrich': ['Institute for Physics and Astronomy, University of Potsdam, D-14476 Potsdam, Germany', 'Max Planck Institute for Gravitational Physics (Albert Einstein Institute), Am M{\\"u}hlenberg 1, D-14476, Germany'],
           'F. Dolon': ['OHP, Observatoire de Haute-Provence, CNRS, Aix Marseille University, Institut Pythéas, St Michel l’Observatoire, France'],
           'D. Dornic': ["CPPM, Aix Marseille Univ, CNRS/IN2P3, CPPM, Marseille, France"],
           'J. Dubouil': ["Astronomie et Systèmes Dynamiques, Institut de Mécanique Céleste et de Calcul des Éphémérides CNRS UMR 8028, Observatoire de Paris, Université PSL, Sorbonne Université, 77 Avenue Denfert-Rochereau, 75014 Paris, France"],                                         
           'J.-G. Ducoin': ['Institut d’Astrophysique de Paris, 98 bis boulevard Arago, 75014 Paris, France'],
           'P.-A. Duverne': ['IJCLab, Univ Paris-Saclay, CNRS/IN2P3, Orsay, France'],
           'A. Esamdin': ['Xinjiang Astronomical Observatory, Chinese Academy of Sciences, Urumqi, Xinjiang 830011, People’s Republic of China', 'University of Chinese Academy of Sciences, Beijing 100049, People’s Republic of China'],
           'A. Fouad': ['National Research Institute of Astronomy and Geophysics, 1 El-marsad St., Helwan, Cairo, Egypt'],
           'F. Guo': ['Physics Department and Astronomy Department, Tsinghua University, Beijing, 100084, People’s Republic of China'],
           'V. Godunova': ['ICAMER Observatory of NAS of Ukraine 27 Acad. Zabolotnoho Str., Kyiv, 03143, Ukraine'],
           'P. Gokuldass': ["Department of Aerospace, Physics, and Space Sciences, Florida Institute of Technology, Melbourne, Florida 32901, USA"],
           'N. Guessoum': ['American University of Sharjah, Physics Department, PO Box 26666, Sharjah, UAE'],
           'E. Gurbanov': ['N.Tusi Shamakhy astrophysical Observatory Azerbaijan National Academy of Sciences, settl.Mamedaliyev, AZ 5626, Shamakhy, Azerbaijan'], 
           'R. Hainich': ['Institut für Physik und Astronomie, Universität Potsdam, Karl-Liebknecht-Str. 24/25, D-14476 Potsdam, Germany'],
           'E. Hasanov': ['N.Tusi Shamakhy astrophysical Observatory Azerbaijan National Academy of Sciences, settl.Mamedaliyev, AZ 5626, Shamakhy, Azerbaijan'], 
           'P. Hello': ['IJCLab, Univ Paris-Saclay, CNRS/IN2P3, Orsay, France'],
           'T. Hussenot-Desenonges': ['IJCLab, Univ Paris-Saclay, CNRS/IN2P3, Orsay, France'], 
           'R. Inasaridze': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia', 'Samtskhe-Javakheti  State  University, Rustaveli Str. 113,  Akhaltsikhe, 0080,  Georgia'],
           'A. Iskandar': ['Xinjiang Astronomical Observatory, Chinese Academy of Sciences, Urumqi, Xinjiang 830011, People’s Republic of China'],
           'E. E. O. Ishida': ['LPC, Université Clermont Auvergne, CNES/IN2P3, F-63000, France'],
           'N. Ismailov': ['N.Tusi Shamakhy astrophysical Observatory Azerbaijan National Academy of Sciences, settl.Mamedaliyev, AZ 5626, Shamakhy, Azerbaijan'],
           'T. Jegou du Laz': ['IJCLab, Univ Paris-Saclay, CNRS/IN2P3, Orsay, France'],
           'D. A. Kann': ["Instituto de Astrof\\'isica de Andaluc\\'ia (IAA-CSIC), Glorieta de la Astronom\\'ia s/n, 18008 Granada, Spain"],
           'G. Kapanadze': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia', 'Samtskhe-Javakheti  State  University, Rustaveli Str. 113,  Akhaltsikhe, 0080,  Georgia'],
           'S. Karpov': ['FZU - Institute of Physics of the Czech Academy of Sciences, Na Slovance 1999/2, CZ-182 21, Praha, Czech Republic'],
           'R. W. Kiendrebeogo': ["Artemis, Observatoire de la Côte d’Azur, Université Côte d’Azur, Boulevard de l'Observatoire, 06304 Nice, France", "Laboratoire de Physique et de Chimie de l’Environnement, Université Joseph KI-ZERBO, Ouagadougou, Burkina Faso"],
           'A. Klotz': ["IRAP, Universit\\'e de Toulouse, CNRS, UPS, 14 Avenue Edouard Belin, F-31400 Toulouse, France", "Universit\\'e Paul Sabatier Toulouse III, Universit\'e de Toulouse, 118 route de Narbonne, 31400 Toulouse, France"],
           'N. Kochiashvili': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia'],
           'A. Kaeouach': ['Observatory of Oukaimden,  Morocco'],
           'J.-P. Kneib': ['Laboratoire d’astrophysique (LASTRO), Ecole Polytechnique F ́ed ́erale de Lausanne (EPFL), Observatoire de Sauverny, CH-1290 Versoix, Switzerland'],
           'W. Kou': ['Beijing Planetarium, Beijing Academy of Science and Technology, Beijing, 100044, People’s Republic of China'],
           'K. Kruiswijk': ['Centre for Cosmology, Particle Physics and Phenomenology - CP3, Universite Catholique de Louvain, B-1348 Louvain-la-Neuve, Belgium'],
           'S. Lombardo': ['Aix Marseille Univ, CNRS, CNES, LAM, Marseille, France'],
           'M. Lamoureux': ["Centre for Cosmology, Particle Physics and Phenomenology - CP3, Universit\\'e catholique de Louvain, B-1348 Louvain-la-Neuve, Belgium"],
           'N. Leroy': ['IJCLab, Univ Paris-Saclay, CNRS/IN2P3, Orsay, France'],
           'A. Le Van Su': ["OHP, Observatoire de Haute-Provence, CNRS, Aix Marseille University, Institut Pythéas, St Michel l’Observatoire, France"],
           'J. Mao': ['Yunnan Observatories, Chinese Academy of Sciences, Kunming 650011, Yunnan, People’s Republic of China'],
           'M. Ma\\v{s}ek': ['FZU - Institute of Physics of the Czech Academy of Sciences, Na Slovance 1999/2, CZ-182 21, Praha, Czech Republic'],
           'T. Midavaine': ["Universit\\'e de Paris, CNRS, Astroparticule et Cosmologie, F-75013 Paris, France"],
           'A. Möller': ['LPC, Université Clermont Auvergne, CNES/IN2P3, F-63000, France', 'Centre for Astrophysics and Supercomputing, Swinburne University of Technology, Mail Number H29, PO Box 218, 31122 Hawthorn, VIC, Australia'],
           'D. Morris': ['University of the Virgin Islands, United States Virgin Islands 00802, USA'],
           'R. Natsvlishvili': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia'],
           'F. Navarete': ["SOAR Telescope/NSF's NOIRLab, Avda Juan Cisternas 1500, 1700000, La Serena, Chile"],
           'S. Nissanke': ["GRAPPA, Anton Pannekoek Institute for Astronomy and Institute of High-Energy Physics, University of Amsterdam, Science Park 904,1098 XH Amsterdam, The Netherlands"],
           'K. Noonan': ["University of the Virgin Islands, United States Virgin Islands 00802, USA"],
           'K. Noysena': ["National Astronomical Research Institute of Thailand (Public Organization), 260, Moo 4, T. Donkaew, A. Mae Rim, Chiang Mai, 50180, Thailand"],
           'N. B. Orange': ['OrangeWave Innovative Science, LLC, Moncks Corner, SC 29461, USA'],
           'J. Peloton': ['IJCLab, Univ Paris-Saclay, CNRS/IN2P3, Orsay, France'],
           'M. Pilloix': ["Artemis, Observatoire de la Côte d’Azur, Université Côte d’Azur, Boulevard de l'Observatoire, 06304 Nice, France"],
           'T. Pradier': ['Université de Strasbourg, CNRS, IPHC UMR 7178, F-67000 Strasbourg, France'],
           'M. Prouza': ['FZU - Institute of Physics of the Czech Academy of Sciences, Na Slovance 1999/2, CZ-182 21, Praha, Czech Republic'],
           'G. Raaijmakers': ["GRAPPA, Anton Pannekoek Institute for Astronomy and Institute of High-Energy Physics, University of Amsterdam, Science Park 904,1098 XH Amsterdam, The Netherlands"],
           'Y. Rajabov': ['Ulugh Beg Astronomical Institute, Uzbekistan Academy of Sciences, Astronomy str. 33, Tashkent 100052, Uzbekistan'],
           'J.-P. Rivet': ['Laboratoire J.-L. Lagrange, Universit de Nice Sophia-Antipolis, CNRS, Observatoire de la Cote d’Azur, F-06304 Nice, France'],
           'Y. Romanyuk': ['Main Astronomical Observatory of National Academy of Sciences of Ukraine, 27 Acad. Zabolotnoho Str., Kyiv, 03143, Ukraine'],
           'L. Rousselot': ["Société Astronomique Populaire du Centre ,40 grande rue, 18340 Arçay, France"],
           'F. Rünger': ['Institut für Physik und Astronomie, Universität Potsdam, Karl-Liebknecht-Str. 24/25, D-14476 Potsdam, Germany'],
           'V. Rupchandani': ['American University of Sharjah, Physics Department, PO Box 26666, Sharjah, UAE', 'Brown University, Providence, RI 02912, United States'],
           'T. Sadibekova': ["Ulugh Beg Astronomical Institute, Uzbekistan Academy of Sciences, Astronomy str. 33, Tashkent 100052, Uzbekistan", "Universit\\'e Paris-Saclay, Universit\\'e Paris Cit\\'e, CEA, CNRS, AIM, 91191, Gif-sur-Yvette, France"],
           'N. Sasaki': ["Laboratório Nacional de Astrofísica, R. dos Estados Unidos, 154 - Nações, Itajubá - MG, 37504-364, Brazil"],
           'K. Smith': ["University of the Virgin Islands, United States Virgin Islands 00802, USA"],
           'O. Sokoliuk': ["Astronomical Observatory\ Taras Shevshenko National University of Kyiv, Observatorna str. 3, Kyiv, 04053, Ukraine", "Main Astronomical Observatory of National Academy of Sciences of Ukraine, 27 Acad. Zabolotnoho Str., Kyiv, 03143, Ukraine"],
           'X. Song': ['Beijing Planetarium, Beijing Academy of Science and Technology, Beijing, 100044, People’s Republic of China'],
           'A. Simon': ["Astronomy and Space Physics Department, Taras Shevchenko National University of Kyiv, Glushkova ave., 4, Kyiv, 03022, Ukraine", "National Center «Junior academy of sciences of Ukraine», 38-44, Dehtiarivska St., Kyiv, 04119, Ukraine"],
           'A. Takey': ['National Research Institute of Astronomy and Geophysics, 1 El-marsad St., Helwan, Cairo, Egypt'],          
           'Y. Tillayev': ['Ulugh Beg Astronomical Institute, Uzbekistan Academy of Sciences, Astronomy str. 33, Tashkent 100052, Uzbekistan', 'National University of Uzbekistan, 4 University str., Tashkent 100174, Uzbekistan'],
           'I. Tosta e Melo': ["INFN, Laboratori Nazionali del Sud, I-95125 Catania, Italy"],
           'D. Turpin': ["Universit\\'e Paris-Saclay, Université Paris Cité, CEA, CNRS, AIM, 91191, Gif-sur-Yvette, France"],
           'A. de Ugarte Postigo': ["Artemis, Observatoire de la Côte d’Azur, Université Côte d’Azur, Boulevard de l'Observatoire, 06304 Nice, France"],
           'M. Vardosanidze': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia', 'Samtskhe-Javakheti  State  University, Rustaveli Str. 113,  Akhaltsikhe, 0080,  Georgia'],
           'X. F. Wang': ['Beijing Planetarium, Beijing Academy of Science and Technology, Beijing, 100044, People’s Republic of China', 'Physics Department and Astronomy Department, Tsinghua University, Beijing, 100084, People’s Republic of China'],
           'G. de Wasseige': ['Laboratoire APC, Université de Paris 10, Rue Alice Domon et Léonie Duquet, 75013 Paris, France'],
           'D. Vernet': ["Observatoire de la Côte d'Azur, CNRS, UMS Galilée, France"],
           'Z. Vidadi': ['N.Tusi Shamakhy astrophysical Observatory Azerbaijan National Academy of Sciences, settl.Mamedaliyev, AZ 5626, Shamakhy, Azerbaijan'],
           'J. Zhu': ['Beijing Planetarium, Beijing Academy of Science and Technology, Beijing, 100044, People’s Republic of China'],
           'Y. Zhu': ['Key Laboratory of Optical Astronomy, National Astronomical Observatories, Chinese Academy of Sciences, A20, Datun Road, Chaoyang District, Beijing 100012, People’s Republic of China'],
    }

institution_list_ordered = []
for key in authors.keys():
    instutions = authors[key]
    for instution in instutions:
        if instution in institution_list_ordered: continue
        institution_list_ordered.append(instution)

print('--------')
print(f"Total {len(authors)} authors") 

nature_style = False
spie_style = True

if nature_style:
    author_list = []
    for key in authors.keys():
        author_institutions = authors[key]
        indices = []
        for author_institution in author_institutions:
            indices.append(institution_list_ordered.index(author_institution))
        author_list.append('%s$^{%s}$' % (key, ",".join([str(x+1) for x in indices])))
    
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
    for key in authors.keys():
        author_institutions = authors[key]
        indices = []
        for author_institution in author_institutions:
            indices.append(institution_list_ordered.index(author_institution))
        author_list.append('\\author[%s]{%s}' % (",".join([str(x+1) for x in indices]), key))

    print("\n".join(author_list))

    institution_list = []
    for ii, institution in enumerate(institution_list_ordered):
        institution_list.append('\\affil[%s]{%s}' % (str(ii+1), institution))
    print("\n".join(institution_list))

