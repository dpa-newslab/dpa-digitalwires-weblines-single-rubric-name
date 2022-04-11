# Multiple rubric_names in dpa's weblines - the ground truth

Sample: ca. 46.000 articles, published in February 2022 and March 2022, spanning around 10.000 different URNs. 
arount 620 of the URNs that are represented several times in the sample carry non-unique combinations 
of rubric_names.

## How often do articles carry multiple `rubric_names`?

|# of rubric_names  |article count  |percent  |
|-------|------:|--------:|
|\[1\]  |36377  |77\.85   |
|\[2\]  |7017   |15\.02   |
|\[3\]  |2683   |5\.74    |
|\[4\]  |516    |1\.10    |
|\[5\]  |110    |0\.24    |
|\[6\]  |25     |0\.05    |



Just out of curiosity, these are two outliers:

  - BVB-Sieg dank Doppelpacker Reus: «Haben Reaktion gezeigt» [urn:newsml:dpa.com:20090101:220213-99-110728]

weblines.infoline_rs.topthemen, weblines.sportsline.fussball.erstebundesliga.news, weblines.sportsline.fussball.erstebundesliga.spielberichte, weblines.sportsline.fussball.news, weblines.sportsline.topnews

-> result of `dpa_rubric_name_heuristics.py`: `weblines.sportsline.fussball`.

  - Schabowski-Zettel: Haus der Geschichte soll Ankauf aufklären [urn:newsml:dpa.com:20090101:220214-99-125264]

weblines.regiolinegeo.berlinbrandenburg, weblines.regiolinegeo.mecklenburgvorpommern, weblines.regiolinegeo.nordrheinwestfalen, weblines.regiolinegeo.sachsen, weblines.regiolinegeo.sachsenanhalt, weblines.regiolinegeo.thueringen

-> result of `dpa_rubric_name_heuristics.py`: `weblines.regiolinegeo.nordrheinwestfalen`.

## How the sample got classified

If you want to inspect the result of our test more closely, please help yourself to the raw data in `urn_rubric_single_rubric.json` (drop_starline = True) and `urn_rubric_single_rubric_starline.json` (drop_starline = False) included in this gist.

Below you see the list of `rubric_names` that remained after applying `dpa_rubric_name_heuristics.py` to our sample data with the flag `drop_starline` set to true.



|rubric\_name                                    |count  |percent  |
|------------------------------------------------|------:|--------:|
|weblines\.infoline\_rs\.boulevard\.entertainment|557    |1\.19    |
|weblines\.infoline\_rs\.boulevard\.kultur       |641    |1\.37    |
|weblines\.infoline\_rs\.eilmeldungen            |107    |0\.23    |
|weblines\.infoline\_rs\.panorama                |1259   |2\.69    |
|weblines\.infoline\_rs\.politik\.ausland        |2107   |4\.51    |
|weblines\.infoline\_rs\.politik\.inland         |1183   |2\.53    |
|weblines\.infoline\_rs\.topthemen               |3      |0\.01    |
|weblines\.infoline\_rs\.wirtschaft              |1304   |2\.79    |
|weblines\.infoline\_rs\.wissenschaft            |213    |0\.46    |
|weblines\.regiolinegeo\.badenwuerttemberg       |2865   |6\.13    |
|weblines\.regiolinegeo\.bayern                  |3115   |6\.67    |
|weblines\.regiolinegeo\.berlinbrandenburg       |3049   |6\.52    |
|weblines\.regiolinegeo\.hamburgschleswigholstein|2452   |5\.25    |
|weblines\.regiolinegeo\.hessen                  |1880   |4\.02    |
|weblines\.regiolinegeo\.mecklenburgvorpommern   |1706   |3\.65    |
|weblines\.regiolinegeo\.niedersachsen           |2188   |4\.68    |
|weblines\.regiolinegeo\.nordrheinwestfalen      |3122   |6\.68    |
|weblines\.regiolinegeo\.rheinlandpfalzsaarland  |1583   |3\.39    |
|weblines\.regiolinegeo\.sachsen                 |1318   |2\.82    |
|weblines\.regiolinegeo\.sachsenanhalt           |905    |1\.94    |
|weblines\.regiolinegeo\.thueringen              |1048   |2\.24    |
|weblines\.serviceline\.auto\-verkehr            |299    |0\.64    |
|weblines\.serviceline\.auto\-verkehr\.aus\-zweiter\-hand|102    |0\.22    |
|weblines\.serviceline\.auto\-verkehr\.autotest  |42     |0\.09    |
|weblines\.serviceline\.auto\-verkehr\.berichte  |297    |0\.64    |
|weblines\.serviceline\.auto\-verkehr\.recht\-im\-verkehr|143    |0\.31    |
|weblines\.serviceline\.digitales                |249    |0\.53    |
|weblines\.serviceline\.digitales\.berichte      |85     |0\.18    |
|weblines\.serviceline\.digitales\.computer\-tipp|60     |0\.13    |
|weblines\.serviceline\.digitales\.spiele        |73     |0\.16    |
|weblines\.serviceline\.digitales\.topapps       |109    |0\.23    |
|weblines\.serviceline\.geld\-recht              |330    |0\.71    |
|weblines\.serviceline\.geld\-recht\.berichte    |159    |0\.34    |
|weblines\.serviceline\.geld\-recht\.steuer\-rat |177    |0\.38    |
|weblines\.serviceline\.gesundheit               |279    |0\.60    |
|weblines\.serviceline\.gesundheit\.berichte     |167    |0\.36    |
|weblines\.serviceline\.gesundheit\.wellness\-und\-fitness|62     |0\.13    |
|weblines\.serviceline\.lifestyle\-mode          |63     |0\.13    |
|weblines\.serviceline\.lifestyle\-mode\.berichte|50     |0\.11    |
|weblines\.serviceline\.reise\-tourismus         |345    |0\.74    |
|weblines\.serviceline\.reise\-tourismus\.berichte|289    |0\.62    |
|weblines\.serviceline\.reise\-tourismus\.deutschland\-reise|114    |0\.24    |
|weblines\.serviceline\.reise\-tourismus\.traumziele|9      |0\.02    |
|weblines\.sportsline\.basketball\.news          |278    |0\.59    |
|weblines\.sportsline\.boxen\.news               |39     |0\.08    |
|weblines\.sportsline\.eishockey\.news           |156    |0\.33    |
|weblines\.sportsline\.fussball                  |1838   |3\.93    |
|weblines\.sportsline\.fussball\.auslandsfussball\.news|383    |0\.82    |
|weblines\.sportsline\.fussball\.championsleague\.news|110    |0\.24    |
|weblines\.sportsline\.fussball\.dfbpokal\.news  |6      |0\.01    |
|weblines\.sportsline\.fussball\.erstebundesliga |2      |0\.00    |
|weblines\.sportsline\.fussball\.erstebundesliga\.news|568    |1\.22    |
|weblines\.sportsline\.fussball\.erstebundesliga\.spielberichte|87     |0\.19    |
|weblines\.sportsline\.fussball\.europaleague\.news|12     |0\.03    |
|weblines\.sportsline\.fussball\.frauen\.news    |173    |0\.37    |
|weblines\.sportsline\.fussball\.nationalmannschaft\.news|87     |0\.19    |
|weblines\.sportsline\.fussball\.news            |255    |0\.55    |
|weblines\.sportsline\.fussball\.wmqualifikation\.news|2      |0\.00    |
|weblines\.sportsline\.fussball\.zweitebundesliga\.news|216    |0\.46    |
|weblines\.sportsline\.fussball\.zweitebundesliga\.spielberichte|58     |0\.12    |
|weblines\.sportsline\.golf\.news                |88     |0\.19    |
|weblines\.sportsline\.handball\.news            |282    |0\.60    |
|weblines\.sportsline\.leichtathletik\.news      |231    |0\.49    |
|weblines\.sportsline\.motorsport                |1      |0\.00    |
|weblines\.sportsline\.motorsport\.formel1\.news |521    |1\.11    |
|weblines\.sportsline\.motorsport\.motorenmix\.news|24     |0\.05    |
|weblines\.sportsline\.pferdesport\.news         |123    |0\.26    |
|weblines\.sportsline\.radsport\.news            |311    |0\.67    |
|weblines\.sportsline\.sportmix\.news            |347    |0\.74    |
|weblines\.sportsline\.sportpolitik\.news        |668    |1\.43    |
|weblines\.sportsline\.tennis\.news              |397    |0\.85    |
|weblines\.sportsline\.topnews                   |7      |0\.01    |
|weblines\.sportsline\.ussport\.news             |501    |1\.07    |
|weblines\.sportsline\.wintersport               |19     |0\.04    |
|weblines\.sportsline\.wintersport\.biathlon\.news|443    |0\.95    |
|weblines\.sportsline\.wintersport\.bob\-schlitten\.news|114    |0\.24    |
|weblines\.sportsline\.wintersport\.skialpin\.news|428    |0\.92    |
|weblines\.sportsline\.wintersport\.skinordisch\.news|390    |0\.83    |
|weblines\.sportsline\.wintersport\.skispringen\.news|269    |0\.58    |
|weblines\.sportsline\.wintersport\.wintermix\.news|319    |0\.68    |
|weblines\.starline\.buch                        |119    |0\.25    |
|weblines\.starline\.fernsehen                   |178    |0\.38    |
|weblines\.starline\.kino                        |178    |0\.38    |
|weblines\.starline\.kulturwelt                  |30     |0\.06    |
|weblines\.starline\.leute                       |221    |0\.47    |
|weblines\.starline\.musik                       |141    |0\.30    |

