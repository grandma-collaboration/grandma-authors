# Author: Michael Coughlin
import os
import sys

authors = {'V. Aivazyan': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia; Ilia State University, Kakutsa Cholokashvili ave 3/5, Tbilisi 0162, Georgia', 'Samtskhe-Javakheti  State  University, Rustaveli Str. 113,  Akhaltsikhe, 0080,  Georgia'],
           'M. Almualla': ['American University of Sharjah, Physics Department, PO Box 26666, Sharjah, UAE'],
           'C. Andrade': ["School of Physics and Astronomy, University of Minnesota, Minneapolis, Minnesota 55455, USA"],
           'S. Antier': ["Artemis, Observatoire de la Côte d’Azur, Université Côte d’Azur, Boulevard de l'Observatoire, 06304 Nice, France", "GRAPPA, Anton Pannekoek Institute for Astronomy and Institute of High-Energy Physics, University of Amsterdam, Science Park 904,1098 XH Amsterdam, The Netherlands", "Universit\'e de Paris, CNRS, Astroparticule et Cosmologie, F-75013 Paris, France"],
           'A. Baransky': ["Astronomical Observatory Taras Shevshenko National University of Kyiv, Observatorna str. 3, Kyiv, 04053, Ukraine"],
           'K. Barynova': ["University of Iceland, Sæmundargata 2, 102 Reykjavík, Iceland"],
           'S. Basa': ["Aix Marseille Univ, CNRS, CNES, LAM, IPhU, Marseille, France"],
           'F. Bayard': ["Société Astronomique de Lyon, 9 Avenue Charles Andr\'e, Saint Genis Laval, France"],
           'S. Beradze': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia; Ilia State University, Kakutsa Cholokashvili ave 3/5, Tbilisi 0162, Georgia', 'Samtskhe-Javakheti  State  University, Rustaveli Str. 113,  Akhaltsikhe, 0080,  Georgia'],
           'D. Berezin': ['ICAMER Observatory of NAS of Ukraine 27 Acad. Zabolotnoho Str., Kyiv, 03143, Ukraine'],
           'M. Blazek': ["Instituto de Astrof\\'isica de Andaluc\\'ia (IAA-CSIC), Glorieta de la Astronom\\'ia s/n, 18008 Granada, Spain"],
           'D. Boutigny': ["Université Grenoble-Alpes, Universit\\'e Savoie Mont Blanc, CNRS/IN2P3 Laboratoire d'Annecy-le-Vieux de Physique des particules, France"],
           'D. Boust': ['Observatoire de Dauban, 04 Banon - France', 'Groupe Astronomique de Querqueville, 61, rue Roger Glinel, 50460, Cherbourg en cotentin, France'],
           'E. Broens': ['Vereniging Voor Sterrenkunde,  Balen-Neetlaan 18A, B-2400, Mol, Belgium', 'Zeeweg 96, B-8200 Brugge, Belgium'],
           'O. Burkhonov': ['Ulugh Beg Astronomical Institute, Uzbekistan Academy of Sciences, Astronomy str. 33, Tashkent 100052, Uzbekistan'],
           'A. Cailleau': ["MP-G2A, Midi Pyr\\'en\\'ees, Groud Astrophysic Addict, 81570, Cuq, France"],
           'D. Cejudo': ['El Center for Backyard Astrophysics, Spain'],
           'N. Christensen': ["Artemis, Observatoire de la Côte d’Azur, Université Côte d’Azur, Boulevard de l'Observatoire, 06304 Nice, France"],
           'A. Coleiro': ["Universit\\'e de Paris, CNRS, Astroparticule et Cosmologie, F-75013 Paris, France"],
           'M. W. Coughlin': ["School of Physics and Astronomy, University of Minnesota, Minneapolis, Minnesota 55455, USA"],
           'T. Culino': ["Artemis, Observatoire de la Côte d’Azur, Université Côte d’Azur, Boulevard de l'Observatoire, 06304 Nice, France"],
           'D. Datashvili': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia; Ilia State University, Kakutsa Cholokashvili ave 3/5, Tbilisi 0162, Georgia', 'Samtskhe-Javakheti  State  University, Rustaveli Str. 113,  Akhaltsikhe, 0080,  Georgia'],
           'T. Dietrich': ['Institute for Physics and Astronomy, University of Potsdam, D-14476 Potsdam, Germany', 'Max Planck Institute for Gravitational Physics (Albert Einstein Institute), Am M{\"u}hlenberg 1, D-14476'],
           'F. Dolon': ['OHP, Observatoire de Haute-Provence, CNRS, Aix Marseille University, Institut Pythéas, St Michel l’Observatoire, France'],
           'D. Dornic': ["CPPM, Aix Marseille Univ, CNRS/IN2P3, CPPM, Marseille, France"],
           'J.-G. Ducoin': ['IJCLab, Univ Paris-Saclay, CNRS/IN2P3, Orsay, France', 'Institut d’Astrophysique de Paris, 98 bis boulevard Arago, 75014 Paris France'],
           'P.-A. Duverne': ['IJCLab, Univ Paris-Saclay, CNRS/IN2P3, Orsay, France'],
           'G. Marchal-Duval': ['IJCLab, Univ Paris-Saclay, CNRS/IN2P3, Orsay, France'],
           'C. Galdies': ['Institute of Earth Systems, University of Malta, MSD 2080, Malta', 'Znith Observatory, Naxxar, Malta'],
           'L. Granier': ['APPAM, Montredon-Labessonnié, France'],
           'V. Godunova': ['ICAMER Observatory of NAS of Ukraine 27 Acad. Zabolotnoho Str., Kyiv, 03143, Ukraine'],
           'P. Gokuldass': ["Department of Aerospace, Physics, and Space Sciences, Florida Institute of Technology, Melbourne, Florida 32901, USA"],
           'H. B. Eggenstein': ['Volkssternwarte Paderborn, Im Schloßpark 13,33104 Paderborn, Germany'],
           'M. Freeberg': ['Hidden Valley Observatory, E9891 810th Ave., Colfax, WI., USA'],
           'N. Guessoum': ['American University of Sharjah, Physics Department, PO Box 26666, Sharjah, UAE'],
           'P. Hello': ['IJCLab, Univ Paris-Saclay, CNRS/IN2P3, Orsay, France'],
           'T. Hussenot-Desenonges': ['IJCLab, Univ Paris-Saclay, CNRS/IN2P3, Orsay, France'], 
           'R. Inasaridze': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia; Ilia State University, Kakutsa Cholokashvili ave 3/5, Tbilisi 0162, Georgia', 'Samtskhe-Javakheti  State  University, Rustaveli Str. 113,  Akhaltsikhe, 0080,  Georgia'],
           'E. E. O. Ishida': ['LPC, Université Clermont Auvergne, CNES/IN2P3, F-63000, France'],
           'P. Jaquiery': ['Dunedin Astronomical Society (DAS), Royal Astronomical Society of New Zealand'],
           'T. Jegou du Laz': ['IJCLab, Univ Paris-Saclay, CNRS/IN2P3, Orsay, France'],
           'D. A. Kann': ["Instituto de Astrof\\'isica de Andaluc\\'ia (IAA-CSIC), Glorieta de la Astronom\\'ia s/n, 18008 Granada, Spain"],
           'G. Kapanadze': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia; Ilia State University, Kakutsa Cholokashvili ave 3/5, Tbilisi 0162, Georgia', 'Samtskhe-Javakheti  State  University, Rustaveli Str. 113,  Akhaltsikhe, 0080,  Georgia'],
           'S. Karpov': ['FZU - Institute of Physics of the Czech Academy of Sciences, Na Slovance 1999/2, CZ-182 21, Praha, Czech Republic'],
           'R. W. Kiendrebeogo': ["Artemis, Observatoire de la Côte d’Azur, Université Côte d’Azur, Boulevard de l'Observatoire, 06304 Nice, France", "Laboratoire de Physique et de Chimie de l’Environnement, Université Joseph KI-ZERBO, Ouagadougou, Burkina Faso"],
           'A. Klotz': ["IRAP, Universit\\'e de Toulouse, CNRS, UPS, 14 Avenue Edouard Belin, F-31400 Toulouse, France", "Universit\\'e Paul Sabatier Toulouse III, Universit\'e de Toulouse, 118 route de Narbonne, 31400 Toulouse, France"],
           'R. Kneip': ["Contern Observatory, L-5316 Contern, Luxembourg"],
           'N. Kochiashvili': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia; Ilia State University, Kakutsa Cholokashvili ave 3/5, Tbilisi 0162, Georgia'],
           'W. Kou': ['Beijing Planetarium, Beijing Academy of Science and Technology, Beijing, 100044, China'],
           'F. Kugel': ['Observatoire de Dauban, 04 Banon - France'],
           'C. Lachaud': ["Universit\\'e de Paris, CNRS, Astroparticule et Cosmologie, F-75013 Paris, France"],
           'M. Lamoureux': ["Centre for Cosmology, Particle Physics and Phenomenology - CP3, Universit\\'e catholique de Louvain, B-1348 Louvain-la-Neuve, Belgium"],
           'S. Leonini': ['Montarrenti Observatory, S.S. 73 Ponente, I-53018, Sovicille, Siena, Italy'],
           'A. Leroy': ['OPERA Z97-, 33820 Saint Palais , France', 'Observatory Uranoscope de l’Ile de France , Allee Camille Flammarion 77220 Gretz –Armainvilliers, France'],
           'N. Leroy': ['IJCLab, Univ Paris-Saclay, CNRS/IN2P3, Orsay, France'],
           'A. Le Van Su': ["OHP, Observatoire de Haute-Provence, CNRS, Aix Marseille University, Institut Pythéas, St Michel l’Observatoire, France"],
           'D. Marchais': ['Observatoire du "Crous des Gats", 31550 Cintegabelle, France'],
           'M. Ma\\v{s}ek': ['FZU - Institute of Physics of the Czech Academy of Sciences, Na Slovance 1999/2, CZ-182 21, Praha, Czech Republic'],
           'T. Midavaine': ["Universit\\'e de Paris, CNRS, Astroparticule et Cosmologie, F-75013 Paris, France"],
           'A. Möller': ['LPC, Université Clermont Auvergne, CNES/IN2P3, F-63000, France', 'Centre for Astrophysics and Supercomputing, Swinburne University of Technology, Mail Number H29, PO Box 218, 31122 Hawthorn, VIC, Australia'],
           'D. Morris': ['University of the Virgin Islands, United States Virgin Islands 00802, USA'],
           'R. Natsvlishvili': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia; Ilia State University, Kakutsa Cholokashvili ave 3/5, Tbilisi 0162, Georgia'],
           'F. Navarete': ["OAR Telescope/NSF's NOIRLab, Avda Juan Cisternas 1500, 1700000, La Serena, Chile"],
           'K. Noysena': ["National Astronomical Research Institute of Thailand (Public Organization), 260, Moo 4, T. Donkaew, A. Mae Rim, Chiang Mai, 50180, Thailand"],
           'S. Nissanke': ["GRAPPA, Anton Pannekoek Institute for Astronomy and Institute of High-Energy Physics, University of Amsterdam, Science Park 904,1098 XH Amsterdam, The Netherlands"],
           'K. Noonan': ['OrangeWave Innovative Science, LLC, Moncks Corner, SC 29461, USA'],
           'N. B. Orange': ['OrangeWave Innovative Science, LLC, Moncks Corner, SC 29461, USA'],
           'J. Peloton': ['IJCLab, Univ Paris-Saclay, CNRS/IN2P3, Orsay, France'],
           'M. Pilloix': ["Artemis, Observatoire de la Côte d’Azur, Université Côte d’Azur, Boulevard de l'Observatoire, 06304 Nice, France"],
           'A. Popowicz': ['Department of Electronics, Electrical Engineering and Microelectronics, Silesian University of Technology, Gliwice, Poland'],
           'T. Pradier': ['Université de Strasbourg, CNRS, IPHC UMR 7178, F-67000 Strasbourg, France'],
           'M. Prouza': ['FZU - Institute of Physics of the Czech Academy of Sciences, Na Slovance 1999/2, CZ-182 21, Praha, Czech Republic'],
           'G. Raaijmakers': ["GRAPPA, Anton Pannekoek Institute for Astronomy and Institute of High-Energy Physics, University of Amsterdam, Science Park 904,1098 XH Amsterdam, The Netherlands"],
           'Y. Rajabov': ['Ulugh Beg Astronomical Institute, Uzbekistan Academy of Sciences, Astronomy str. 33, Tashkent 100052, Uzbekistan'],
           'M. Richmond': ['School of Physics and Astronomy, Rochester Institute of Technology, 84 Lomb Memorial Drive, Rochester, NY 14623, USA'],
           'Ya. Romanyuk': ['Main Astronomical Observatory of National Academy of Sciences of Ukraine, 27 Acad. Zabolotnoho Str., Kyiv, 03143, Ukraine'],
           'L. Rousselot': ["Société Astronomique Populaire du Centre ,40 grande rue, 18340 Arçay, France"],
           'V. Rupchandani': ['American University of Sharjah, Physics Department, PO Box 26666, Sharjah, UAE'],
           'T. Sadibekova': ["Ulugh Beg Astronomical Institute, Uzbekistan Academy of Sciences, Astronomy str. 33, Tashkent 100052, Uzbekistan", "Universit\'e Paris-Saclay, Universit\'e Paris Cit\'e, CEA, CNRS, AIM, 91191, Gif-sur-Yvette, France"],
           'M. Serrau': ['Observatoire de Dauban, 04 Banon - France'],
           'O. Sokoliuk': ["Astronomical Observatory\ Taras Shevshenko National University of Kyiv, Observatorna str. 3, Kyiv, 04053, Ukraine", "Main Astronomical Observatory of National Academy of Sciences of Ukraine, 27 Acad. Zabolotnoho Str., Kyiv, 03143, Ukraine"],
           'X. Song': ['Beijing Planetarium, Beijing Academy of Science and Technology, Beijing, 100044, China'],
           'A. Simon': ["Astronomy and Space Physics Department, Taras Shevchenko National University of Kyiv, Glushkova ave., 4, Kyiv, 03022, Ukraine", "National Center «Junior academy of sciences of Ukraine», 38-44, Dehtiarivska St., Kyiv, 04119, Ukraine"],
           'C. Stachie': ["Artemis, Observatoire de la Côte d’Azur, Université Côte d’Azur, Boulevard de l'Observatoire, 06304 Nice, France"],
           'A. Taylor': ['Institute of Gravitational Research, University of Glasgow, Glasgow, G12 8QQ', 'ICAstronomy, Oria, Almería, Spain', 'Deep Sky Chile, Pichasca, Rio Hurtado, Chile'],
           'Y. Tillayev': ['Ulugh Beg Astronomical Institute, Uzbekistan Academy of Sciences, Astronomy str. 33, Tashkent 100052, Uzbekistan', 'National University of Uzbekistan, 4 University str., Tashkent 100174, Uzbekistan'],
           'D. Turpin': ["Université Paris-Saclay, Université Paris Cité, CEA, CNRS, AIM, 91191, Gif-sur-Yvette, France"],
           'M. Vardosanidze': ['E. Kharadze Georgian National Astrophysical Observatory, Mt.Kanobili, Abastumani, 0301, Adigeni, Georgia; Ilia State University, Kakutsa Cholokashvili ave 3/5, Tbilisi 0162, Georgia', 'Samtskhe-Javakheti  State  University, Rustaveli Str. 113,  Akhaltsikhe, 0080,  Georgia'],
           'J. Vlieghe': ["IJCLab, Univ Paris-Saclay, CNRS/IN2P3, Orsay, France"],
           'I. Tosta e Melo': ["INFN, Laboratori Nazionali del Sud, I-95125 Catania, Italy"],
           'X. F. Wang': ['Beijing Planetarium, Beijing Academy of Science and Technology, Beijing, 100044, China', 'Physics Department and Astronomy Department, Tsinghua University, Beijing, 100084, China'],
           'J. Zhu': ['Beijing Planetarium, Beijing Academy of Science and Technology, Beijing, 100044, China'],
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

