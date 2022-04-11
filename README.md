# digitalwires: Choosing a single rubric_name


dpa editors often choose a list of `rubric_names` for their articles, in order to represent better what a story is about. 
This makes the metadata for the story richer and more accurate. But it also can create a problem if you must assign exactly one `rubric_name` because of your CMS or any other system where you store dpa items, or because the menu on the website where you publish dpa items forces you to do so. 

Here are some examples for use cases of more than one `rubric_name`:

   * a story about a flood emergency or a soccer/football match might be important in two regions, i.e. Bayern and Baden-Württemberg - and consequently may carry two `rubric_names` (`weblines.regiolinegeo.bayern` and `weblines.regiolinegeo.badenwuerttemberg`).

   * some `rubric_names` are used to signal "this is currently a top story" for 3-12 hours, they convey no or little information about the general topic and are removed before choosing the single `rubric_name`. For example `weblines.sportsline.topnews`.
   
   * `weblines.infoline_rs.boulevard.*` and `weblines.starline.*` overlap in many instances, for example an item might be assigned to `rubric_names` `weblines.infoline_rs.boulevard.kultur` and `weblines.starline.kino`. In these cases, the starline `rubric_name` is dropped if the flag `drop_starline` is true, which is the default. If the flag is false, the `weblines.starline.*` `rubric_name` is preferred if both are present. 


This gist has python example code on how to boil down the list. Please see [dpa_rubric_name_heuristics.py](dpa_rubric_name_heuristics.py) for more details, it is heavily documented.

The official list of `rubric_names` is available for Download at our [API Portal](https://api-portal.dpa-newslab.com/doc/format#hinweise-f%C3%BCr-bezieher-der-dpa-weblines-im-nitf-format), a [copy](20220405_qcodes_rubric.csv) is held in this repo for convenience. Please consider that the local repository is most probably outdated by the time you read this, and use the original.

We did an [empirical test](DETAILS.md) of the algorithm, to be reasonably sure it works in practice.

