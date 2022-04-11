from typing import List

# dpa tags some stories with several rubric_names. The python code below can boil that down to one



# This is the sentinel value returned if the code cannot find a single rubric_name. 
UNDECIDED = 'xxx-no-single-rubric-name-chosen'

# The rubric_name segments below are used to signal "this is currently a top story" for 3-12 hours
# they convey no or little information about the general topic and are removed before choosing 
# the single rubric_name.
#
# Sometimes, zero `rubric_names` remain after removing topnews signal rubric_names.
# In this case, the topnews `rubric_name`s are sorted in the order listed below and 
# and the first one is chosen

topnews_preference = { f'{key}': value
        for value, key in enumerate((
    '.sportsline.topnews',
    '.topnews',
    '.topthemen',
    '.top-news'
))}

# sometimes, stories fit into two general news `rubric_names`. If so, the first one on the list is chosen

infoline_preference = { f'weblines.infoline_rs.{key}': value
        for value, key in enumerate((
        'panorama',
        'wirtschaft',
        'politik.inland',
        'politik.ausland',
        'wissenschaft',
        'eilmeldungen'
))}

# regionlinegeo stories are somtimes assigned more than one rubric_name if the story concerns
# more than one dpa region. If there are several rubric_names for regionlinegeo, the first that 
# appears on the list below is selected
# the list below would be one that prefers south german regions over north german regions

regionline_preference = { f'weblines.regiolinegeo.{key}': value
        for value, key in enumerate((
        'badenwuerttemberg',
        'bayern',
        'nordrheinwestfalen',
        'hamburgschleswigholstein',
        'mecklenburgvorpommern',
        'berlinbrandenburg',
        'niedersachsen',
        'hessen',
        'rheinlandpfalzsaarland',
        'thueringen',
        'sachsenanhalt',
        'sachsen',
))}



# sometimes, stories fit into two starline `rubric_names`. If so, the first one on the list is chosen
starline_preference = { f'weblines.starline.{key}': value
        for value, key in enumerate((
        'fernsehen',
        'kino',
        'kunst',
        'leute',
        'leute.geburtstage',
        'musik',
        'buch',
        'leben',
        'kulturwelt'
))}


# sometimes, stories fit into two sportsline `rubric_names`. If so, the first one on the list is chosen
sportsline_preference = { f'weblines.sportsline.{key}': value
        for value, key in enumerate((
        'basketball',
        'handball',
        'boxen',
        'e-sport',
        'eishockey',
        'fussball',
        'golf',
        'leichtathletik',
        'motorsport',
        'pferdesport',
        'radsport',
        'sportmix',
        'sportpolitik',
        'tennis',
        'ussport',
        'wintersport'
))}
 



def topn(name:str, depth: int) -> str:
    """ utility function to cut the hierarchy short after n dots"""
    return ".".join(name.split(".")[:depth]) 

# sportsline or serviceline items carry many rubric_names by default - see list below.
# These are narrowed down to the top 4 or top 3 hierarchy, if it is unique, in the case below "weblines.sportsline.fussball"
# 
#    weblines.sportsline.fussball.erstebundesliga.news
#    weblines.sportsline.fussball.europaleague.news
#    weblines.sportsline.fussball.news
#


def consolidate_topn(names: List[str]) -> str:
    for length in range(4,2,-1):
        top_n = set((topn(name, length) for name in names))
        if len(top_n) == 1:
            return list(top_n)[0]
    return UNDECIDED

#
#  the main logic starts here
# 
#
# weblines.infoline_rs and weblines.starline overlap in many instances
# for example an item might be assigned `rubric_name`s 
# weblines.infoline_rs.boulevard.kultur and weblines.starline.kino
# in these cases, the starline `rubric_name` is dropped if drop_starline is True

def boildown_regionline(names: List[str]) -> str:
    """
    more than one regionlinegeo ? select preferred
    """
    if any(('regiolinegeo' in name for name in names)):
        return sorted(names, key=
                lambda name: regionline_preference.get(name, 100))[0]
    return UNDECIDED


def boildown_starline(names: List[str]) -> str:
    """
    more than one starline ? select preferred
    """
    starline_names = [ name for name in names if "starline" in name ]
    if len(starline_names) == 0:
     return UNDECIDED
    if len(starline_names)==1:
       return starline_names[0]
    else:
        starlines = [ { "rubric": rubric , "key": starline_preference[rubric] }
                for rubric in starline_names ] 
        return sorted(starlines, key = lambda a: a["key"])[0]["rubric"]


def boildown_infoline(names: List[str]) -> str:
    """
    more than one infoline_rs ? select preferred
    """
    if any(('infoline_rs' in name for name in names)):
        return sorted(names, key=
                lambda name: infoline_preference.get(name, 100))[0]
    return UNDECIDED


def boildown_sportsline(names: List[str]) -> str:
    """
    more than one sportsline ? try to consolidate on top 3 or 4, or else select preferred
    """
    if any(('sportsline' in name for name in names)):
        single = consolidate_topn(names)
        if single != UNDECIDED:
            return single
        else: 
            sportslines = [ { "rubric": rubric , "key": "%03d%s" % (sportsline_preference[topn(rubric, 3)],rubric) }
                    for rubric in names
                    if "sportsline" in rubric ]
            return sorted(sportslines, key = lambda a: a["key"])[0]["rubric"]
    else:
        return UNDECIDED

def boildown_serviceline(names: List[str]) -> str:
    """
    # more than one serviceline? try to consolidate on top 3 or 4  
    """
    if any(('serviceline' in name for name in names)):
        single = consolidate_topn(names)
        return single
    else:
        return UNDECIDED


def rubric_name(names: List[str], drop_starline: bool = True ) -> str: 
    # one rubric_name -> take it
    if len(names) == 1:
        return names[0]
    # remove "top news signal" rubric_names 
    non_topnews = list(( 
                    name
                    for name in names
                    if not any((name.endswith(signal) 
                        for signal in topnews_preference.keys()))
                  ))
    # one rubric_name left -> take it
    if len(non_topnews) == 1:
        return non_topnews[0]
    # in some rare cases, articles have only top news and no specific section
    if len(non_topnews) == 0:
        # sort by order in topnews_preference
        sorted_topnews = sorted(names, 
                    key = lambda rubric: min((pref if rubric.endswith(name) else 9999 
                    for name,pref  in topnews_preference.items()))
                    )
        return sorted_topnews[0]
    # try the lines one by one, the 
    # first one that succeeds wins
    # you may reorder this if you find that infoline should be considered before regioline for example
    for boildown_method in (
            boildown_regionline,
            boildown_starline if not drop_starline else lambda a: UNDECIDED or a,
            boildown_infoline,
            boildown_sportsline,
            boildown_starline,
            boildown_serviceline
            ):
        result = boildown_method(non_topnews)
        if result != UNDECIDED:
            return result
    # should never happen
    return UNDECIDED

