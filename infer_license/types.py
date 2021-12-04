from dataclasses import dataclass, field
from typing import Optional, Set

import pkg_resources


@dataclass
class License:
    name: str  # SPDX Full name
    shortname: str  # SPDX Identifier
    trove_classifier: Optional[str]

    # For lazy loading
    _text: Optional[str] = field(default=None, repr=False)
    _trigrams: Optional[Set[str]] = field(default=None, repr=False)

    @property
    def text(self) -> str:
        if not self._text:
            self._text = pkg_resources.resource_string(
                __name__, f"licenses/{self.shortname}.txt"
            ).decode()
        return self._text

    @property
    def trigrams(self) -> Set[str]:
        if not self._trigrams:
            self._trigrams = trigrams(self.text)
        assert self._trigrams is not None
        return self._trigrams


def trigrams(text: str) -> Set[str]:
    words = [w for w in text.split() if w not in ("/*", "*", "*/", "#")]
    return {f"{words[i]}-{words[i+1]}-{words[i+2]}" for i in range(len(words) - 3)}


# See some discussion at https://github.com/pypa/warehouse/issues/2996 about
# using SPDX names, which is what we use for shortname.  Several do not have
# Trove classifiers available.
KNOWN_LICENSES = [
    License(
        "Apache License 2.0",
        "Apache-2.0",
        "License :: OSI Approved :: Apache Software License",
    ),
    License(
        'BSD 2-Clause "Simplified" License',
        "BSD-2-Clause",
        "License :: OSI Approved :: BSD License",
    ),
    License(
        'BSD 3-Clause "New" or "Revised" License',
        "BSD-3-Clause",
        "License :: OSI Approved :: BSD License",
    ),
    License("Creative Commons Attribution 4.0 International", "CC-BY-4.0", None),
    License(
        "GNU Affero General Public License v3.0 or later",
        "AGPL-3.0-or-later",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
    ),
    License(
        "GNU Lesser General Public License v2 or later",
        "LGPL-2.0-or-later",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
    ),
    License(
        "GNU Lesser General Public License v2.1 or later", "LGPL-2.1-or-later", None,
    ),
    License(
        "GNU Lesser General Public License v3.0 or later",
        "LGPL-3.0-or-later",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
    ),
    License(
        "GNU General Public License v2.0 or later",
        "GPL-2.0-or-later",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
    ),
    License(
        "GNU General Public License v3.0 or later",
        "GPL-3.0-or-later",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    ),
    License("MIT License", "MIT", "License :: OSI Approved :: MIT License"),
    License("MIT No Attribution", "MIT-0", "License :: OSI Approved :: MIT License"),
    License("X11 License", "X11", None),
    # This one is a bit unusual; the license text I include is verbatim from the
    # Python distribution, not from https://spdx.org/licenses/Python-2.0.html
    License(
        "Python License 2.0",
        "Python-2.0",
        "License :: OSI Approved :: Python Software Foundation License",
    ),
    # From SPDX-license-list-text
    License(
        "BSD Zero Clause License",
        "0BSD",
        "License :: OSI Approved :: BSD Zero Clause License (0BSD)",
    ),
    License(
        "Attribution Assurance License",
        "AAL",
        "License :: OSI Approved :: Attribution Assurance License (AAL)",
    ),
    License("Abstyles License", "Abstyles", None),
    License(
        "Adobe Systems Incorporated Source Code License Agreement", "Adobe-2006", None
    ),
    License("Adobe Glyph List License", "Adobe-Glyph", None),
    License("Amazon Digital Services License", "ADSL", None),
    License(
        "Academic Free License v1.1",
        "AFL-1.1",
        "License :: OSI Approved :: Academic Free License v1.1 (AFL-1.1)",
    ),
    License(
        "Academic Free License v1.2",
        "AFL-1.2",
        "License :: OSI Approved :: Academic Free License v1.2 (AFL-1.2)",
    ),
    License(
        "Academic Free License v2.0",
        "AFL-2.0",
        "License :: OSI Approved :: Academic Free License v2.0 (AFL-2.0)",
    ),
    License(
        "Academic Free License v2.1",
        "AFL-2.1",
        "License :: OSI Approved :: Academic Free License v2.1 (AFL-2.1)",
    ),
    License(
        "Academic Free License v3.0",
        "AFL-3.0",
        "License :: OSI Approved :: Academic Free License v3.0 (AFL-3.0)",
    ),
    License("Afmparse License", "Afmparse", None),
    License("Affero General Public License v1.0 only", "AGPL-1.0-only", None),
    License("Affero General Public License v1.0 or later", "AGPL-1.0-or-later", None),
    License(
        "GNU Affero General Public License v3.0 only",
        "AGPL-3.0-only",
        "License :: OSI Approved :: GNU Affero General Public License v3.0 only (AGPL-3.0-only)",
    ),
    License(
        "GNU Affero General Public License v3.0 or later",
        "AGPL-3.0-or-later",
        "License :: OSI Approved :: GNU Affero General Public License v3.0 or later (AGPL-3.0-or-later)",
    ),
    License("Aladdin Free Public License", "Aladdin", "License :: Aladdin Free Public License (AFPL)"),
    License("AMD's plpa_map.c License", "AMDPLPA", None),
    License("Apple MIT License", "AML", None),
    License("Academy of Motion Picture Arts and Sciences BSD", "AMPAS", None),
    License("ANTLR Software Rights Notice", "ANTLR-PD", None),
    License(
        "ANTLR Software Rights Notice with license fallback", "ANTLR-PD-fallback", None
    ),
    License("Apache License 1.0", "Apache-1.0", None),
    License(
        "Apache License 1.1",
        "Apache-1.1",
        "License :: OSI Approved :: Apache License 1.1 (Apache-1.1)",
    ),
    License(
        "Apache License 2.0",
        "Apache-2.0",
        "License :: OSI Approved :: Apache License 2.0 (Apache-2.0)",
    ),
    License("Adobe Postscript AFM License", "APAFML", None),
    License(
        "Adaptive Public License 1.0",
        "APL-1.0",
        "License :: OSI Approved :: Adaptive Public License 1.0 (APL-1.0)",
    ),
    License(
        "Apple Public Source License 1.0",
        "APSL-1.0",
        "License :: OSI Approved :: Apple Public Source License 1.0 (APSL-1.0)",
    ),
    License(
        "Apple Public Source License 1.1",
        "APSL-1.1",
        "License :: OSI Approved :: Apple Public Source License 1.1 (APSL-1.1)",
    ),
    License(
        "Apple Public Source License 1.2",
        "APSL-1.2",
        "License :: OSI Approved :: Apple Public Source License 1.2 (APSL-1.2)",
    ),
    License(
        "Apple Public Source License 2.0",
        "APSL-2.0",
        "License :: OSI Approved :: Apple Public Source License 2.0 (APSL-2.0)",
    ),
    License(
        "Artistic License 1.0",
        "Artistic-1.0",
        "License :: OSI Approved :: Artistic License 1.0 (Artistic-1.0)",
    ),
    License(
        "Artistic License 1.0 w/clause 8",
        "Artistic-1.0-cl8",
        "License :: OSI Approved :: Artistic License 1.0 w/clause 8 (Artistic-1.0-cl8)",
    ),
    License(
        "Artistic License 1.0 (Perl)",
        "Artistic-1.0-Perl",
        "License :: OSI Approved :: Artistic License 1.0 (Perl) (Artistic-1.0-Perl)",
    ),
    License(
        "Artistic License 2.0",
        "Artistic-2.0",
        "License :: OSI Approved :: Artistic License 2.0 (Artistic-2.0)",
    ),
    License("Bahyph License", "Bahyph", None),
    License("Barr License", "Barr", None),
    License("Beerware License", "Beerware", None),
    License("BitTorrent Open Source License v1.0", "BitTorrent-1.0", None),
    License("BitTorrent Open Source License v1.1", "BitTorrent-1.1", None),
    License("SQLite Blessing", "blessing", None),
    License("Blue Oak Model License 1.0.0", "BlueOak-1.0.0", None),
    License("Borceux license", "Borceux", None),
    License(
        "BSD 1-Clause License",
        "BSD-1-Clause",
        "License :: OSI Approved :: BSD 1-Clause License (BSD-1-Clause)",
    ),
    License(
        'BSD 2-Clause"Simplified License',
        "BSD-2-Clause",
        'License :: OSI Approved :: BSD 2-Clause"Simplified" License (BSD-2-Clause)',
    ),
    License(
        "BSD-2-Clause Plus Patent License",
        "BSD-2-Clause-Patent",
        "License :: OSI Approved :: BSD-2-Clause Plus Patent License (BSD-2-Clause-Patent)",
    ),
    License("BSD 2-Clause with views sentence", "BSD-2-Clause-Views", None),
    License(
        'BSD 3-Clause"New" or"Revised" License',
        "BSD-3-Clause",
        'License :: OSI Approved :: BSD 3-Clause"New" or"Revised" License (BSD-3-Clause)',
    ),
    License("BSD with attribution", "BSD-3-Clause-Attribution", None),
    License("BSD 3-Clause Clear License", "BSD-3-Clause-Clear", None),
    License(
        "Lawrence Berkeley National Labs BSD variant license",
        "BSD-3-Clause-LBNL",
        "License :: OSI Approved :: Lawrence Berkeley National Labs BSD variant license (BSD-3-Clause-LBNL)",
    ),
    License("BSD 3-Clause Modification", "BSD-3-Clause-Modification", None),
    License(
        "BSD 3-Clause No Military License", "BSD-3-Clause-No-Military-License", None
    ),
    License("BSD 3-Clause No Nuclear License", "BSD-3-Clause-No-Nuclear-License", None),
    License(
        "BSD 3-Clause No Nuclear License 2014",
        "BSD-3-Clause-No-Nuclear-License-2014",
        None,
    ),
    License(
        "BSD 3-Clause No Nuclear Warranty", "BSD-3-Clause-No-Nuclear-Warranty", None
    ),
    License("BSD 3-Clause Open MPI variant", "BSD-3-Clause-Open-MPI", None),
    License('BSD 4-Clause"Original" or"Old" License', "BSD-4-Clause", None),
    License("BSD 4 Clause Shortened", "BSD-4-Clause-Shortened", None),
    License(
        "BSD-4-Clause (University of California-Specific)", "BSD-4-Clause-UC", None
    ),
    License("BSD Protection License", "BSD-Protection", None),
    License("BSD Source Code Attribution", "BSD-Source-Code", None),
    License(
        "Boost Software License 1.0",
        "BSL-1.0",
        "License :: OSI Approved :: Boost Software License 1.0 (BSL-1.0)",
    ),
    License("Business Source License 1.1", "BUSL-1.1", None),
    License("bzip2 and libbzip2 License v1.0.5", "bzip2-1.0.5", None),
    License("bzip2 and libbzip2 License v1.0.6", "bzip2-1.0.6", None),
    License("Computational Use of Data Agreement v1.0", "C-UDA-1.0", None),
    License(
        "Cryptographic Autonomy License 1.0",
        "CAL-1.0",
        "License :: OSI Approved :: Cryptographic Autonomy License 1.0 (CAL-1.0)",
    ),
    License(
        "Cryptographic Autonomy License 1.0 (Combined Work Exception)",
        "CAL-1.0-Combined-Work-Exception",
        "License :: OSI Approved :: Cryptographic Autonomy License 1.0 (Combined Work Exception) (CAL-1.0-Combined-Work-Exception)",
    ),
    License("Caldera License", "Caldera", None),
    License(
        "Computer Associates Trusted Open Source License 1.1",
        "CATOSL-1.1",
        "License :: OSI Approved :: Computer Associates Trusted Open Source License 1.1 (CATOSL-1.1)",
    ),
    License("Creative Commons Attribution 1.0 Generic", "CC-BY-1.0", None),
    License("Creative Commons Attribution 2.0 Generic", "CC-BY-2.0", None),
    License("Creative Commons Attribution 2.5 Generic", "CC-BY-2.5", None),
    License("Creative Commons Attribution 2.5 Australia", "CC-BY-2.5-AU", None),
    License("Creative Commons Attribution 3.0 Unported", "CC-BY-3.0", None),
    License("Creative Commons Attribution 3.0 Austria", "CC-BY-3.0-AT", None),
    License("Creative Commons Attribution 3.0 Germany", "CC-BY-3.0-DE", None),
    License("Creative Commons Attribution 3.0 Netherlands", "CC-BY-3.0-NL", None),
    License("Creative Commons Attribution 3.0 United States", "CC-BY-3.0-US", None),
    License("Creative Commons Attribution 4.0 International", "CC-BY-4.0", None),
    License(
        "Creative Commons Attribution Non Commercial 1.0 Generic", "CC-BY-NC-1.0", None
    ),
    License(
        "Creative Commons Attribution Non Commercial 2.0 Generic", "CC-BY-NC-2.0", None
    ),
    License(
        "Creative Commons Attribution Non Commercial 2.5 Generic", "CC-BY-NC-2.5", None
    ),
    License(
        "Creative Commons Attribution Non Commercial 3.0 Unported", "CC-BY-NC-3.0", None
    ),
    License(
        "Creative Commons Attribution Non Commercial 3.0 Germany",
        "CC-BY-NC-3.0-DE",
        None,
    ),
    License(
        "Creative Commons Attribution Non Commercial 4.0 International",
        "CC-BY-NC-4.0",
        None,
    ),
    License(
        "Creative Commons Attribution Non Commercial No Derivatives 1.0 Generic",
        "CC-BY-NC-ND-1.0",
        None,
    ),
    License(
        "Creative Commons Attribution Non Commercial No Derivatives 2.0 Generic",
        "CC-BY-NC-ND-2.0",
        None,
    ),
    License(
        "Creative Commons Attribution Non Commercial No Derivatives 2.5 Generic",
        "CC-BY-NC-ND-2.5",
        None,
    ),
    License(
        "Creative Commons Attribution Non Commercial No Derivatives 3.0 Unported",
        "CC-BY-NC-ND-3.0",
        None,
    ),
    License(
        "Creative Commons Attribution Non Commercial No Derivatives 3.0 Germany",
        "CC-BY-NC-ND-3.0-DE",
        None,
    ),
    License(
        "Creative Commons Attribution Non Commercial No Derivatives 3.0 IGO",
        "CC-BY-NC-ND-3.0-IGO",
        None,
    ),
    License(
        "Creative Commons Attribution Non Commercial No Derivatives 4.0 International",
        "CC-BY-NC-ND-4.0",
        None,
    ),
    License(
        "Creative Commons Attribution Non Commercial Share Alike 1.0 Generic",
        "CC-BY-NC-SA-1.0",
        None,
    ),
    License(
        "Creative Commons Attribution Non Commercial Share Alike 2.0 Generic",
        "CC-BY-NC-SA-2.0",
        None,
    ),
    License(
        "Creative Commons Attribution-NonCommercial-ShareAlike 2.0 France",
        "CC-BY-NC-SA-2.0-FR",
        None,
    ),
    License(
        "Creative Commons Attribution Non Commercial Share Alike 2.0 England and Wales",
        "CC-BY-NC-SA-2.0-UK",
        None,
    ),
    License(
        "Creative Commons Attribution Non Commercial Share Alike 2.5 Generic",
        "CC-BY-NC-SA-2.5",
        None,
    ),
    License(
        "Creative Commons Attribution Non Commercial Share Alike 3.0 Unported",
        "CC-BY-NC-SA-3.0",
        None,
    ),
    License(
        "Creative Commons Attribution Non Commercial Share Alike 3.0 Germany",
        "CC-BY-NC-SA-3.0-DE",
        None,
    ),
    License(
        "Creative Commons Attribution Non Commercial Share Alike 3.0 IGO",
        "CC-BY-NC-SA-3.0-IGO",
        None,
    ),
    License(
        "Creative Commons Attribution Non Commercial Share Alike 4.0 International",
        "CC-BY-NC-SA-4.0",
        None,
    ),
    License(
        "Creative Commons Attribution No Derivatives 1.0 Generic", "CC-BY-ND-1.0", None
    ),
    License(
        "Creative Commons Attribution No Derivatives 2.0 Generic", "CC-BY-ND-2.0", None
    ),
    License(
        "Creative Commons Attribution No Derivatives 2.5 Generic", "CC-BY-ND-2.5", None
    ),
    License(
        "Creative Commons Attribution No Derivatives 3.0 Unported", "CC-BY-ND-3.0", None
    ),
    License(
        "Creative Commons Attribution No Derivatives 3.0 Germany",
        "CC-BY-ND-3.0-DE",
        None,
    ),
    License(
        "Creative Commons Attribution No Derivatives 4.0 International",
        "CC-BY-ND-4.0",
        None,
    ),
    License(
        "Creative Commons Attribution Share Alike 1.0 Generic", "CC-BY-SA-1.0", None
    ),
    License(
        "Creative Commons Attribution Share Alike 2.0 Generic", "CC-BY-SA-2.0", None
    ),
    License(
        "Creative Commons Attribution Share Alike 2.0 England and Wales",
        "CC-BY-SA-2.0-UK",
        None,
    ),
    License(
        "Creative Commons Attribution Share Alike 2.1 Japan", "CC-BY-SA-2.1-JP", None
    ),
    License(
        "Creative Commons Attribution Share Alike 2.5 Generic", "CC-BY-SA-2.5", None
    ),
    License(
        "Creative Commons Attribution Share Alike 3.0 Unported", "CC-BY-SA-3.0", None
    ),
    License(
        "Creative Commons Attribution Share Alike 3.0 Austria", "CC-BY-SA-3.0-AT", None
    ),
    License(
        "Creative Commons Attribution Share Alike 3.0 Germany", "CC-BY-SA-3.0-DE", None
    ),
    License(
        "Creative Commons Attribution Share Alike 4.0 International",
        "CC-BY-SA-4.0",
        None,
    ),
    License(
        "Creative Commons Public Domain Dedication and Certification", "CC-PDDC", None
    ),
    License("Creative Commons Zero v1.0 Universal", "CC0-1.0", "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication"),
    License(
        "Common Development and Distribution License 1.0",
        "CDDL-1.0",
        "License :: OSI Approved :: Common Development and Distribution License 1.0 (CDDL-1.0)",
    ),
    License("Common Development and Distribution License 1.1", "CDDL-1.1", None),
    License("Common Documentation License 1.0", "CDL-1.0", None),
    License(
        "Community Data License Agreement Permissive 1.0", "CDLA-Permissive-1.0", None
    ),
    License(
        "Community Data License Agreement Permissive 2.0", "CDLA-Permissive-2.0", None
    ),
    License("Community Data License Agreement Sharing 1.0", "CDLA-Sharing-1.0", None),
    License("CeCILL Free Software License Agreement v1.0", "CECILL-1.0", None),
    License("CeCILL Free Software License Agreement v1.1", "CECILL-1.1", None),
    License("CeCILL Free Software License Agreement v2.0", "CECILL-2.0", None),
    License(
        "CeCILL Free Software License Agreement v2.1",
        "CECILL-2.1",
        "License :: OSI Approved :: CeCILL Free Software License Agreement v2.1 (CECILL-2.1)",
    ),
    License("CeCILL-B Free Software License Agreement", "CECILL-B", "License :: CeCILL-B Free Software License Agreement (CECILL-B)"),
    License("CeCILL-C Free Software License Agreement", "CECILL-C", "License :: CeCILL-C Free Software License Agreement (CECILL-C)"),
    License("CERN Open Hardware Licence v1.1", "CERN-OHL-1.1", None),
    License("CERN Open Hardware Licence v1.2", "CERN-OHL-1.2", None),
    License(
        "CERN Open Hardware Licence Version 2 - Permissive",
        "CERN-OHL-P-2.0",
        "License :: OSI Approved :: CERN Open Hardware Licence Version 2 - Permissive (CERN-OHL-P-2.0)",
    ),
    License(
        "CERN Open Hardware Licence Version 2 - Strongly Reciprocal",
        "CERN-OHL-S-2.0",
        "License :: OSI Approved :: CERN Open Hardware Licence Version 2 - Strongly Reciprocal (CERN-OHL-S-2.0)",
    ),
    License(
        "CERN Open Hardware Licence Version 2 - Weakly Reciprocal",
        "CERN-OHL-W-2.0",
        "License :: OSI Approved :: CERN Open Hardware Licence Version 2 - Weakly Reciprocal (CERN-OHL-W-2.0)",
    ),
    License("Clarified Artistic License", "ClArtistic", None),
    License("CNRI Jython License", "CNRI-Jython", None),
    License(
        "CNRI Python License",
        "CNRI-Python",
        "License :: OSI Approved :: CNRI Python License (CNRI-Python)",
    ),
    License(
        "CNRI Python Open Source GPL Compatible License Agreement",
        "CNRI-Python-GPL-Compatible",
        None,
    ),
    License("Copyfree Open Innovation License", "COIL-1.0", None),
    License("Community Specification License 1.0", "Community-Spec-1.0", None),
    License("Condor Public License v1.1", "Condor-1.1", None),
    License("copyleft-next 0.3.0", "copyleft-next-0.3.0", None),
    License("copyleft-next 0.3.1", "copyleft-next-0.3.1", None),
    License(
        "Common Public Attribution License 1.0",
        "CPAL-1.0",
        "License :: OSI Approved :: Common Public Attribution License 1.0 (CPAL-1.0)",
    ),
    License(
        "Common Public License 1.0",
        "CPL-1.0",
        "License :: OSI Approved :: Common Public License 1.0 (CPL-1.0)",
    ),
    License("Code Project Open License 1.02", "CPOL-1.02", None),
    License("Crossword License", "Crossword", None),
    License("CrystalStacker License", "CrystalStacker", None),
    License(
        "CUA Office Public License v1.0",
        "CUA-OPL-1.0",
        "License :: OSI Approved :: CUA Office Public License v1.0 (CUA-OPL-1.0)",
    ),
    License("Cube License", "Cube", None),
    License("curl License", "curl", None),
    License("Deutsche Freie Software Lizenz", "D-FSL-1.0", None),
    License("diffmark license", "diffmark", None),
    License("DOC License", "DOC", None),
    License("Dotseqn License", "Dotseqn", None),
    License("Detection Rule License 1.0", "DRL-1.0", None),
    License("DSDP License", "DSDP", None),
    License("dvipdfm License", "dvipdfm", None),
    License(
        "Educational Community License v1.0",
        "ECL-1.0",
        "License :: OSI Approved :: Educational Community License v1.0 (ECL-1.0)",
    ),
    License(
        "Educational Community License v2.0",
        "ECL-2.0",
        "License :: OSI Approved :: Educational Community License v2.0 (ECL-2.0)",
    ),
    License(
        "Eiffel Forum License v1.0",
        "EFL-1.0",
        "License :: OSI Approved :: Eiffel Forum License v1.0 (EFL-1.0)",
    ),
    License(
        "Eiffel Forum License v2.0",
        "EFL-2.0",
        "License :: OSI Approved :: Eiffel Forum License v2.0 (EFL-2.0)",
    ),
    License("eGenix.com Public License 1.1.0", "eGenix", None),
    License(
        "Entessa Public License v1.0",
        "Entessa",
        "License :: OSI Approved :: Entessa Public License v1.0 (Entessa)",
    ),
    License("EPICS Open License", "EPICS", None),
    License(
        "Eclipse Public License 1.0",
        "EPL-1.0",
        "License :: OSI Approved :: Eclipse Public License 1.0 (EPL-1.0)",
    ),
    License(
        "Eclipse Public License 2.0",
        "EPL-2.0",
        "License :: OSI Approved :: Eclipse Public License 2.0 (EPL-2.0)",
    ),
    License("Erlang Public License v1.1", "ErlPL-1.1", None),
    License("Etalab Open License 2.0", "etalab-2.0", None),
    License(
        "EU DataGrid Software License",
        "EUDatagrid",
        "License :: OSI Approved :: EU DataGrid Software License (EUDatagrid)",
    ),
    License("European Union Public License 1.0", "EUPL-1.0", None),
    License(
        "European Union Public License 1.1",
        "EUPL-1.1",
        "License :: OSI Approved :: European Union Public License 1.1 (EUPL-1.1)",
    ),
    License(
        "European Union Public License 1.2",
        "EUPL-1.2",
        "License :: OSI Approved :: European Union Public License 1.2 (EUPL-1.2)",
    ),
    License("Eurosym License", "Eurosym", None),
    License("Fair License", "Fair", "License :: OSI Approved :: Fair License (Fair)"),
    License("Fraunhofer FDK AAC Codec Library", "FDK-AAC", None),
    License(
        "Frameworx Open License 1.0",
        "Frameworx-1.0",
        "License :: OSI Approved :: Frameworx Open License 1.0 (Frameworx-1.0)",
    ),
    License("FreeBSD Documentation License", "FreeBSD-DOC", None),
    License("FreeImage Public License v1.0", "FreeImage", None),
    License("FSF All Permissive License", "FSFAP", None),
    License("FSF Unlimited License", "FSFUL", None),
    License("FSF Unlimited License (with License Retention)", "FSFULLR", None),
    License("Freetype Project License", "FTL", None),
    License("GD License", "GD", None),
    License(
        "GNU Free Documentation License v1.1 only - invariants",
        "GFDL-1.1-invariants-only",
        None,
    ),
    License(
        "GNU Free Documentation License v1.1 or later - invariants",
        "GFDL-1.1-invariants-or-later",
        None,
    ),
    License(
        "GNU Free Documentation License v1.1 only - no invariants",
        "GFDL-1.1-no-invariants-only",
        None,
    ),
    License(
        "GNU Free Documentation License v1.1 or later - no invariants",
        "GFDL-1.1-no-invariants-or-later",
        None,
    ),
    License("GNU Free Documentation License v1.1 only", "GFDL-1.1-only", None),
    License("GNU Free Documentation License v1.1 or later", "GFDL-1.1-or-later", None),
    License(
        "GNU Free Documentation License v1.2 only - invariants",
        "GFDL-1.2-invariants-only",
        None,
    ),
    License(
        "GNU Free Documentation License v1.2 or later - invariants",
        "GFDL-1.2-invariants-or-later",
        None,
    ),
    License(
        "GNU Free Documentation License v1.2 only - no invariants",
        "GFDL-1.2-no-invariants-only",
        None,
    ),
    License(
        "GNU Free Documentation License v1.2 or later - no invariants",
        "GFDL-1.2-no-invariants-or-later",
        None,
    ),
    License("GNU Free Documentation License v1.2 only", "GFDL-1.2-only", None),
    License("GNU Free Documentation License v1.2 or later", "GFDL-1.2-or-later", None),
    License(
        "GNU Free Documentation License v1.3 only - invariants",
        "GFDL-1.3-invariants-only",
        None,
    ),
    License(
        "GNU Free Documentation License v1.3 or later - invariants",
        "GFDL-1.3-invariants-or-later",
        None,
    ),
    License(
        "GNU Free Documentation License v1.3 only - no invariants",
        "GFDL-1.3-no-invariants-only",
        None,
    ),
    License(
        "GNU Free Documentation License v1.3 or later - no invariants",
        "GFDL-1.3-no-invariants-or-later",
        None,
    ),
    License("GNU Free Documentation License v1.3 only", "GFDL-1.3-only", None),
    License("GNU Free Documentation License v1.3 or later", "GFDL-1.3-or-later", None),
    License("Giftware License", "Giftware", None),
    License("GL2PS License", "GL2PS", None),
    License("3dfx Glide License", "Glide", None),
    License("Glulxe License", "Glulxe", None),
    License("Good Luck With That Public License", "GLWTPL", None),
    License("gnuplot License", "gnuplot", None),
    License("GNU General Public License v1.0 only", "GPL-1.0-only", None),
    License("GNU General Public License v1.0 or later", "GPL-1.0-or-later", None),
    License(
        "GNU General Public License v2.0 only",
        "GPL-2.0-only",
        "License :: OSI Approved :: GNU General Public License v2.0 only (GPL-2.0-only)",
    ),
    License(
        "GNU General Public License v2.0 or later",
        "GPL-2.0-or-later",
        "License :: OSI Approved :: GNU General Public License v2.0 or later (GPL-2.0-or-later)",
    ),
    License(
        "GNU General Public License v3.0 only",
        "GPL-3.0-only",
        "License :: OSI Approved :: GNU General Public License v3.0 only (GPL-3.0-only)",
    ),
    License(
        "GNU General Public License v3.0 or later",
        "GPL-3.0-or-later",
        "License :: OSI Approved :: GNU General Public License v3.0 or later (GPL-3.0-or-later)",
    ),
    License("gSOAP Public License v1.3b", "gSOAP-1.3b", None),
    License("Haskell Language Report License", "HaskellReport", None),
    License("Hippocratic License 2.1", "Hippocratic-2.1", None),
    License(
        "Historical Permission Notice and Disclaimer",
        "HPND",
        "License :: OSI Approved :: Historical Permission Notice and Disclaimer (HPND)",
    ),
    License(
        "Historical Permission Notice and Disclaimer - sell variant",
        "HPND-sell-variant",
        None,
    ),
    License("HTML Tidy License", "HTMLTIDY", None),
    License("IBM PowerPC Initialization and Boot Software", "IBM-pibs", None),
    License("ICU License", "ICU", None),
    License("Independent JPEG Group License", "IJG", None),
    License("ImageMagick License", "ImageMagick", None),
    License("iMatix Standard Function Library Agreement", "iMatix", None),
    License("Imlib2 License", "Imlib2", None),
    License("Info-ZIP License", "Info-ZIP", None),
    License(
        "Intel Open Source License",
        "Intel",
        "License :: OSI Approved :: Intel Open Source License (Intel)",
    ),
    License("Intel ACPI Software License Agreement", "Intel-ACPI", None),
    License("Interbase Public License v1.0", "Interbase-1.0", None),
    License(
        "IPA Font License", "IPA", "License :: OSI Approved :: IPA Font License (IPA)"
    ),
    License(
        "IBM Public License v1.0",
        "IPL-1.0",
        "License :: OSI Approved :: IBM Public License v1.0 (IPL-1.0)",
    ),
    License("ISC License", "ISC", "License :: OSI Approved :: ISC License (ISC)"),
    License("JasPer License", "JasPer-2.0", None),
    License("Japan Network Information Center License", "JPNIC", None),
    License("JSON License", "JSON", None),
    License("Licence Art Libre 1.2", "LAL-1.2", None),
    License("Licence Art Libre 1.3", "LAL-1.3", None),
    License("Latex2e License", "Latex2e", None),
    License("Leptonica License", "Leptonica", None),
    License(
        "GNU Library General Public License v2 only",
        "LGPL-2.0-only",
        "License :: OSI Approved :: GNU Library General Public License v2 only (LGPL-2.0-only)",
    ),
    License(
        "GNU Library General Public License v2 or later",
        "LGPL-2.0-or-later",
        "License :: OSI Approved :: GNU Library General Public License v2 or later (LGPL-2.0-or-later)",
    ),
    License(
        "GNU Lesser General Public License v2.1 only",
        "LGPL-2.1-only",
        "License :: OSI Approved :: GNU Lesser General Public License v2.1 only (LGPL-2.1-only)",
    ),
    License(
        "GNU Lesser General Public License v2.1 or later",
        "LGPL-2.1-or-later",
        "License :: OSI Approved :: GNU Lesser General Public License v2.1 or later (LGPL-2.1-or-later)",
    ),
    License(
        "GNU Lesser General Public License v3.0 only",
        "LGPL-3.0-only",
        "License :: OSI Approved :: GNU Lesser General Public License v3.0 only (LGPL-3.0-only)",
    ),
    License(
        "GNU Lesser General Public License v3.0 or later",
        "LGPL-3.0-or-later",
        "License :: OSI Approved :: GNU Lesser General Public License v3.0 or later (LGPL-3.0-or-later)",
    ),
    License("Lesser General Public License For Linguistic Resources", "LGPLLR", None),
    License("libpng License", "Libpng", None),
    License("PNG Reference Library version 2", "libpng-2.0", None),
    License("libselinux public domain notice", "libselinux-1.0", None),
    License("libtiff License", "libtiff", None),
    License(
        "Licence Libre du Québec – Permissive version 1.1",
        "LiLiQ-P-1.1",
        "License :: OSI Approved :: Licence Libre du Québec – Permissive version 1.1 (LiLiQ-P-1.1)",
    ),
    License(
        "Licence Libre du Québec – Réciprocité version 1.1",
        "LiLiQ-R-1.1",
        "License :: OSI Approved :: Licence Libre du Québec – Réciprocité version 1.1 (LiLiQ-R-1.1)",
    ),
    License(
        "Licence Libre du Québec – Réciprocité forte version 1.1",
        "LiLiQ-Rplus-1.1",
        "License :: OSI Approved :: Licence Libre du Québec – Réciprocité forte version 1.1 (LiLiQ-Rplus-1.1)",
    ),
    License("Linux man-pages Copyleft", "Linux-man-pages-copyleft", None),
    License("Linux Kernel Variant of OpenIB.org license", "Linux-OpenIB", None),
    License(
        "Lucent Public License Version 1.0",
        "LPL-1.0",
        "License :: OSI Approved :: Lucent Public License Version 1.0 (LPL-1.0)",
    ),
    License(
        "Lucent Public License v1.02",
        "LPL-1.02",
        "License :: OSI Approved :: Lucent Public License v1.02 (LPL-1.02)",
    ),
    License("LaTeX Project Public License v1.0", "LPPL-1.0", None),
    License("LaTeX Project Public License v1.1", "LPPL-1.1", None),
    License("LaTeX Project Public License v1.2", "LPPL-1.2", None),
    License("LaTeX Project Public License v1.3a", "LPPL-1.3a", None),
    License(
        "LaTeX Project Public License v1.3c",
        "LPPL-1.3c",
        "License :: OSI Approved :: LaTeX Project Public License v1.3c (LPPL-1.3c)",
    ),
    License("MakeIndex License", "MakeIndex", None),
    License(
        "The MirOS Licence",
        "MirOS",
        "License :: OSI Approved :: The MirOS Licence (MirOS)",
    ),
    License("MIT License", "MIT", "License :: OSI Approved :: MIT License (MIT)"),
    License(
        "MIT No Attribution",
        "MIT-0",
        "License :: OSI Approved :: MIT No Attribution (MIT-0)",
    ),
    License("Enlightenment License (e16)", "MIT-advertising", None),
    License("CMU License", "MIT-CMU", None),
    License("enna License", "MIT-enna", None),
    License("feh License", "MIT-feh", None),
    License(
        "MIT License Modern Variant",
        "MIT-Modern-Variant",
        "License :: OSI Approved :: MIT License Modern Variant (MIT-Modern-Variant)",
    ),
    License("MIT Open Group variant", "MIT-open-group", None),
    License("MIT +no-false-attribs license", "MITNFA", None),
    License(
        "Motosoto License",
        "Motosoto",
        "License :: OSI Approved :: Motosoto License (Motosoto)",
    ),
    License("mpich2 License", "mpich2", None),
    License(
        "Mozilla Public License 1.0",
        "MPL-1.0",
        "License :: OSI Approved :: Mozilla Public License 1.0 (MPL-1.0)",
    ),
    License(
        "Mozilla Public License 1.1",
        "MPL-1.1",
        "License :: OSI Approved :: Mozilla Public License 1.1 (MPL-1.1)",
    ),
    License(
        "Mozilla Public License 2.0",
        "MPL-2.0",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL-2.0)",
    ),
    License(
        "Mozilla Public License 2.0 (no copyleft exception)",
        "MPL-2.0-no-copyleft-exception",
        "License :: OSI Approved :: Mozilla Public License 2.0 (no copyleft exception) (MPL-2.0-no-copyleft-exception)",
    ),
    License(
        "Microsoft Public License",
        "MS-PL",
        "License :: OSI Approved :: Microsoft Public License (MS-PL)",
    ),
    License(
        "Microsoft Reciprocal License",
        "MS-RL",
        "License :: OSI Approved :: Microsoft Reciprocal License (MS-RL)",
    ),
    License("Matrix Template Library License", "MTLL", None),
    License("Mulan Permissive Software License, Version 1", "MulanPSL-1.0", None),
    License(
        "Mulan Permissive Software License, Version 2",
        "MulanPSL-2.0",
        "License :: OSI Approved :: Mulan Permissive Software License, Version 2 (MulanPSL-2.0)",
    ),
    License(
        "Multics License",
        "Multics",
        "License :: OSI Approved :: Multics License (Multics)",
    ),
    License("Mup License", "Mup", None),
    License(
        "Nara Institute of Science and Technology License (2003)", "NAIST-2003", None
    ),
    License(
        "NASA Open Source Agreement 1.3",
        "NASA-1.3",
        "License :: OSI Approved :: NASA Open Source Agreement 1.3 (NASA-1.3)",
    ),
    License(
        "Naumen Public License",
        "Naumen",
        "License :: OSI Approved :: Naumen Public License (Naumen)",
    ),
    License("Net Boolean Public License v1", "NBPL-1.0", None),
    License("Non-Commercial Government Licence", "NCGL-UK-2.0", None),
    License(
        "University of Illinois/NCSA Open Source License",
        "NCSA",
        "License :: OSI Approved :: University of Illinois/NCSA Open Source License (NCSA)",
    ),
    License("Net-SNMP License", "Net-SNMP", None),
    License("NetCDF license", "NetCDF", None),
    License("Newsletr License", "Newsletr", None),
    License(
        "Nethack General Public License",
        "NGPL",
        "License :: OSI Approved :: Nethack General Public License (NGPL)",
    ),
    License("NIST Public Domain Notice", "NIST-PD", None),
    License(
        "NIST Public Domain Notice with license fallback", "NIST-PD-fallback", None
    ),
    License("Norwegian Licence for Open Government Data (NLOD) 1.0", "NLOD-1.0", None),
    License("Norwegian Licence for Open Government Data (NLOD) 2.0", "NLOD-2.0", None),
    License("No Limit Public License", "NLPL", None),
    License(
        "Nokia Open Source License",
        "Nokia",
        "License :: OSI Approved :: Nokia Open Source License (Nokia)",
    ),
    License("Netizen Open Source License", "NOSL", None),
    License("Noweb License", "Noweb", None),
    License("Netscape Public License v1.0", "NPL-1.0", None),
    License("Netscape Public License v1.1", "NPL-1.1", None),
    License(
        "Non-Profit Open Software License 3.0",
        "NPOSL-3.0",
        "License :: OSI Approved :: Non-Profit Open Software License 3.0 (NPOSL-3.0)",
    ),
    License("NRL License", "NRL", None),
    License("NTP License", "NTP", "License :: OSI Approved :: NTP License (NTP)"),
    License("NTP No Attribution", "NTP-0", None),
    License("Open Use of Data Agreement v1.0", "O-UDA-1.0", None),
    License("Open CASCADE Technology Public License", "OCCT-PL", None),
    License(
        "OCLC Research Public License 2.0",
        "OCLC-2.0",
        "License :: OSI Approved :: OCLC Research Public License 2.0 (OCLC-2.0)",
    ),
    License("Open Data Commons Open Database License v1.0", "ODbL-1.0", None),
    License("Open Data Commons Attribution License v1.0", "ODC-By-1.0", None),
    License("SIL Open Font License 1.0", "OFL-1.0", None),
    License(
        "SIL Open Font License 1.0 with no Reserved Font Name", "OFL-1.0-no-RFN", None
    ),
    License("SIL Open Font License 1.0 with Reserved Font Name", "OFL-1.0-RFN", None),
    License(
        "SIL Open Font License 1.1",
        "OFL-1.1",
        "License :: OSI Approved :: SIL Open Font License 1.1 (OFL-1.1)",
    ),
    License(
        "SIL Open Font License 1.1 with no Reserved Font Name",
        "OFL-1.1-no-RFN",
        "License :: OSI Approved :: SIL Open Font License 1.1 with no Reserved Font Name (OFL-1.1-no-RFN)",
    ),
    License(
        "SIL Open Font License 1.1 with Reserved Font Name",
        "OFL-1.1-RFN",
        "License :: OSI Approved :: SIL Open Font License 1.1 with Reserved Font Name (OFL-1.1-RFN)",
    ),
    License("OGC Software License, Version 1.0", "OGC-1.0", None),
    License(
        "Taiwan Open Government Data License, version 1.0", "OGDL-Taiwan-1.0", None
    ),
    License("Open Government Licence - Canada", "OGL-Canada-2.0", None),
    License("Open Government Licence v1.0", "OGL-UK-1.0", None),
    License("Open Government Licence v2.0", "OGL-UK-2.0", None),
    License("Open Government Licence v3.0", "OGL-UK-3.0", None),
    License(
        "Open Group Test Suite License",
        "OGTSL",
        "License :: OSI Approved :: Open Group Test Suite License (OGTSL)",
    ),
    License("Open LDAP Public License v1.1", "OLDAP-1.1", None),
    License("Open LDAP Public License v1.2", "OLDAP-1.2", None),
    License("Open LDAP Public License v1.3", "OLDAP-1.3", None),
    License("Open LDAP Public License v1.4", "OLDAP-1.4", None),
    License(
        "Open LDAP Public License v2.0 (or possibly 2.0A and 2.0B)", "OLDAP-2.0", None
    ),
    License("Open LDAP Public License v2.0.1", "OLDAP-2.0.1", None),
    License("Open LDAP Public License v2.1", "OLDAP-2.1", None),
    License("Open LDAP Public License v2.2", "OLDAP-2.2", None),
    License("Open LDAP Public License v2.2.1", "OLDAP-2.2.1", None),
    License("Open LDAP Public License 2.2.2", "OLDAP-2.2.2", None),
    License("Open LDAP Public License v2.3", "OLDAP-2.3", None),
    License("Open LDAP Public License v2.4", "OLDAP-2.4", None),
    License("Open LDAP Public License v2.5", "OLDAP-2.5", None),
    License("Open LDAP Public License v2.6", "OLDAP-2.6", None),
    License("Open LDAP Public License v2.7", "OLDAP-2.7", None),
    License(
        "Open LDAP Public License v2.8",
        "OLDAP-2.8",
        "License :: OSI Approved :: Open LDAP Public License v2.8 (OLDAP-2.8)",
    ),
    License("Open Market License", "OML", None),
    License("OpenSSL License", "OpenSSL", None),
    License("Open Public License v1.0", "OPL-1.0", None),
    License("Open Publication License v1.0", "OPUBL-1.0", None),
    License(
        "OSET Public License version 2.1",
        "OSET-PL-2.1",
        "License :: OSI Approved :: OSET Public License version 2.1 (OSET-PL-2.1)",
    ),
    License(
        "Open Software License 1.0",
        "OSL-1.0",
        "License :: OSI Approved :: Open Software License 1.0 (OSL-1.0)",
    ),
    License("Open Software License 1.1", "OSL-1.1", None),
    License(
        "Open Software License 2.0",
        "OSL-2.0",
        "License :: OSI Approved :: Open Software License 2.0 (OSL-2.0)",
    ),
    License(
        "Open Software License 2.1",
        "OSL-2.1",
        "License :: OSI Approved :: Open Software License 2.1 (OSL-2.1)",
    ),
    License(
        "Open Software License 3.0",
        "OSL-3.0",
        "License :: OSI Approved :: Open Software License 3.0 (OSL-3.0)",
    ),
    License("The Parity Public License 6.0.0", "Parity-6.0.0", None),
    License("The Parity Public License 7.0.0", "Parity-7.0.0", None),
    License(
        "Open Data Commons Public Domain Dedication & License 1.0", "PDDL-1.0", None
    ),
    License(
        "PHP License v3.0",
        "PHP-3.0",
        "License :: OSI Approved :: PHP License v3.0 (PHP-3.0)",
    ),
    License(
        "PHP License v3.01",
        "PHP-3.01",
        "License :: OSI Approved :: PHP License v3.01 (PHP-3.01)",
    ),
    License("Plexus Classworlds License", "Plexus", None),
    License(
        "PolyForm Noncommercial License 1.0.0", "PolyForm-Noncommercial-1.0.0", None
    ),
    License(
        "PolyForm Small Business License 1.0.0", "PolyForm-Small-Business-1.0.0", None
    ),
    License(
        "PostgreSQL License",
        "PostgreSQL",
        "License :: OSI Approved :: PostgreSQL License (PostgreSQL)",
    ),
    License("Python Software Foundation License 2.0", "PSF-2.0", None),
    License("psfrag License", "psfrag", None),
    License("psutils License", "psutils", None),
    License(
        "Python License 2.0",
        "Python-2.0",
        "License :: OSI Approved :: Python License 2.0 (Python-2.0)",
    ),
    License("Qhull License", "Qhull", None),
    License(
        "Q Public License 1.0",
        "QPL-1.0",
        "License :: OSI Approved :: Q Public License 1.0 (QPL-1.0)",
    ),
    License("Rdisc License", "Rdisc", None),
    License("Red Hat eCos Public License v1.1", "RHeCos-1.1", None),
    License(
        "Reciprocal Public License 1.1",
        "RPL-1.1",
        "License :: OSI Approved :: Reciprocal Public License 1.1 (RPL-1.1)",
    ),
    License(
        "Reciprocal Public License 1.5",
        "RPL-1.5",
        "License :: OSI Approved :: Reciprocal Public License 1.5 (RPL-1.5)",
    ),
    License(
        "RealNetworks Public Source License v1.0",
        "RPSL-1.0",
        "License :: OSI Approved :: RealNetworks Public Source License v1.0 (RPSL-1.0)",
    ),
    License("RSA Message-Digest License", "RSA-MD", None),
    License(
        "Ricoh Source Code Public License",
        "RSCPL",
        "License :: OSI Approved :: Ricoh Source Code Public License (RSCPL)",
    ),
    License("Ruby License", "Ruby", None),
    License("Sax Public Domain Notice", "SAX-PD", None),
    License("Saxpath License", "Saxpath", None),
    License("SCEA Shared Source License", "SCEA", None),
    License("Scheme Language Report License", "SchemeReport", None),
    License("Sendmail License", "Sendmail", None),
    License("Sendmail License 8.23", "Sendmail-8.23", None),
    License("SGI Free Software License B v1.0", "SGI-B-1.0", None),
    License("SGI Free Software License B v1.1", "SGI-B-1.1", None),
    License("SGI Free Software License B v2.0", "SGI-B-2.0", None),
    License("Solderpad Hardware License v0.5", "SHL-0.5", None),
    License("Solderpad Hardware License, Version 0.51", "SHL-0.51", None),
    License(
        "Simple Public License 2.0",
        "SimPL-2.0",
        "License :: OSI Approved :: Simple Public License 2.0 (SimPL-2.0)",
    ),
    License(
        "Sun Industry Standards Source License v1.1",
        "SISSL",
        "License :: OSI Approved :: Sun Industry Standards Source License v1.1 (SISSL)",
    ),
    License("Sun Industry Standards Source License v1.2", "SISSL-1.2", None),
    License(
        "Sleepycat License",
        "Sleepycat",
        "License :: OSI Approved :: Sleepycat License (Sleepycat)",
    ),
    License("Standard ML of New Jersey License", "SMLNJ", None),
    License("Secure Messaging Protocol Public License", "SMPPL", None),
    License("SNIA Public License 1.1", "SNIA", None),
    License("Spencer License 86", "Spencer-86", None),
    License("Spencer License 94", "Spencer-94", None),
    License("Spencer License 99", "Spencer-99", None),
    License(
        "Sun Public License v1.0",
        "SPL-1.0",
        "License :: OSI Approved :: Sun Public License v1.0 (SPL-1.0)",
    ),
    License("SSH OpenSSH license", "SSH-OpenSSH", None),
    License("SSH short notice", "SSH-short", None),
    License("Server Side Public License, v 1", "SSPL-1.0", None),
    License("SugarCRM Public License v1.1.3", "SugarCRM-1.1.3", None),
    License("Scheme Widget Library (SWL) Software License Agreement", "SWL", None),
    License("TAPR Open Hardware License v1.0", "TAPR-OHL-1.0", None),
    License("TCL/TK License", "TCL", None),
    License("TCP Wrappers License", "TCP-wrappers", None),
    License("TMate Open Source License", "TMate", None),
    License("TORQUE v2.5+ Software License v1.1", "TORQUE-1.1", None),
    License("Trusster Open Source License", "TOSL", None),
    License("Technische Universitaet Berlin License 1.0", "TU-Berlin-1.0", None),
    License("Technische Universitaet Berlin License 2.0", "TU-Berlin-2.0", None),
    License(
        "Upstream Compatibility License v1.0",
        "UCL-1.0",
        "License :: OSI Approved :: Upstream Compatibility License v1.0 (UCL-1.0)",
    ),
    License(
        "Unicode License Agreement - Data Files and Software (2015)",
        "Unicode-DFS-2015",
        None,
    ),
    License(
        "Unicode License Agreement - Data Files and Software (2016)",
        "Unicode-DFS-2016",
        "License :: OSI Approved :: Unicode License Agreement - Data Files and Software (2016) (Unicode-DFS-2016)",
    ),
    License("Unicode Terms of Use", "Unicode-TOU", None),
    License(
        "The Unlicense",
        "Unlicense",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
    ),
    License(
        "Universal Permissive License v1.0",
        "UPL-1.0",
        "License :: OSI Approved :: Universal Permissive License v1.0 (UPL-1.0)",
    ),
    License("Vim License", "Vim", None),
    License("VOSTROM Public License for Open Source", "VOSTROM", None),
    License(
        "Vovida Software License v1.0",
        "VSL-1.0",
        "License :: OSI Approved :: Vovida Software License v1.0 (VSL-1.0)",
    ),
    License(
        "W3C Software Notice and License (2002-12-31)",
        "W3C",
        "License :: OSI Approved :: W3C Software Notice and License (2002-12-31) (W3C)",
    ),
    License("W3C Software Notice and License (1998-07-20)", "W3C-19980720", None),
    License(
        "W3C Software Notice and Document License (2015-05-13)", "W3C-20150513", None
    ),
    License(
        "Sybase Open Watcom Public License 1.0",
        "Watcom-1.0",
        "License :: OSI Approved :: Sybase Open Watcom Public License 1.0 (Watcom-1.0)",
    ),
    License("Wsuipa License", "Wsuipa", None),
    License("Do What The F*ck You Want To Public License", "WTFPL", None),
    License("X11 License", "X11", None),
    License("Xerox License", "Xerox", None),
    License("XFree86 License 1.1", "XFree86-1.1", None),
    License("xinetd License", "xinetd", None),
    License("X.Net License", "Xnet", "License :: OSI Approved :: X.Net License (Xnet)"),
    License("XPP License", "xpp", None),
    License("XSkat License", "XSkat", None),
    License("Yahoo! Public License v1.0", "YPL-1.0", None),
    License("Yahoo! Public License v1.1", "YPL-1.1", None),
    License("Zed License", "Zed", None),
    License("Zend License v2.0", "Zend-2.0", None),
    License("Zimbra Public License v1.3", "Zimbra-1.3", None),
    License("Zimbra Public License v1.4", "Zimbra-1.4", None),
    License("zlib License", "Zlib", "License :: OSI Approved :: zlib License (Zlib)"),
    License("zlib/libpng License with Acknowledgement", "zlib-acknowledgement", None),
    License("Zope Public License 1.1", "ZPL-1.1", None),
    License(
        "Zope Public License 2.0",
        "ZPL-2.0",
        "License :: OSI Approved :: Zope Public License 2.0 (ZPL-2.0)",
    ),
    License(
        "Zope Public License 2.1",
        "ZPL-2.1",
        "License :: OSI Approved :: Zope Public License 2.1 (ZPL-2.1)",
    ),
]


def license_by_shortname(shortname: str) -> License:
    for el in KNOWN_LICENSES:
        if el.shortname == shortname:
            return el
    raise KeyError(f"Unknown license: {shortname!r}")
