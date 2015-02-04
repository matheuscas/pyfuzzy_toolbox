from pyfuzzy_toolbox import preprocessing as pre

# Cornel Movie Review 2
text_1 = "`oh behave !" + \
    " \nfelicity shagwell is one shagadellic babe ." + \
    " \ndo i make your horny ?" +\
    " \nfemale fembots with breasts that require gun controlling ." + \
    " \nanything that resembles bananas and two balls of icecream ." +\
    " \nthe nut-biting finale between mini me and austin ." +\
    " \nall that body hair is a real turn on , it's a pity more leading men don't wear it on screen ." +\
    " \nanything that vaguely resembles sausages and eggs ." +\
    " \nfat bastard ." +\
    " \nthe love scene between felicity and fat bastard , that redefines sex ." +\
    " \nthe wrongly implied love scene in the tent that redefines anal sex ." +\
    " \nthe love scene between austin and ivana humpalot , that redefines chess and oral sex ." +\
    " \nthe love scene between dr ." +\
    " evil and frau farbissina , that redefines weird sex ." +\
    " \nthe love affair between austin and felicity , that does not happen , because his mojo goes missing ." +\
    " \nthe relationship between dr evil , himself and mini me which redefines a solo love affair ." +\
    " \nthe unique relationship between dr evil and his son scott www ." +\
    " com ." +\
    " zip , that says a lot about our relationship with our children nowadays ." +\
    " \nweanies , johnny , richard , dick etc . '" +\
    " \nthis movie is every bit as silly and crazy as the first ." +\
    " \nthere are moments that will make your sick , which are probably best forgotten , but overall mike myers has redefined what it means to be an international spy and leading man . \n"

# The sentence '" \nthe love scene between dr ."' is considered a sentece,
# cuz the dot is separated from 'dr' The parses loses itself.

text_1a = "this feature is like a double header , two sets of clich ?" +\
    " s for the price of one ." +\
    " \nnot only do we get the usual tired sports chestnuts , but the banal rich girl-poor boy love story is tossed in for good measure ." +\
    " \nan original moment in this loser is as rare as a chicago cubs world series appearance ." +\
    " \nthe screenplay by kevin falls and john gatins , based on a story by falls , merely lobs its plotline at the audience ." +\
    " \nthis is a story that needed sent down for seasoning and more coaching ." +\
    " \nsummer catch centers around ryan dunne ( freddie prinze jr . ) , a cape cod youth chosen to participate in the prestigious cape cod baseball league , supposedly a showcase for the best young amateur and college players in the country ." +\
    " \nryan is a blue-collar kind of guy ." +\
    " \nhe works with his dad taking care of the lawns of cape cod's rich and famous ." +\
    " \nhe also , as we are informed early , his own worst enemy ." +\
    " \nhe has the potential and the talent , but always seems to self-destruct at the crucial moment ." +\
    " \nso , ryan tries to remained focused on baseball ." +\
    " \nthen he meets tenley parrish ( jessica biel ) , daughter of one of the blue bloods whose lawn he manicures ." +\
    " \ntenley , a name only a hack screenwriter could invent , is unlike her snobbish counterparts and falls for ryan ." +\
    " \nif you can't figure out where all this nonsense leads , then you need a remedial course in film viewing ." +\
    " \nas always prinze is pretty to look at , but his performance mainly consists of facial expressions : puppy dog love , heartbreak , frustration , self-loathing or determination ." +\
    " \nbiel cries a lot , while bruce davison merely acts smarmy as her class-conscious father ." +\
    " \nthe only beacon is matthew lillard's fun-loving billy brubaker , the team's catcher ." +\
    " \nsummer catch borrows situations and stylings from other baseball movies , such as bull durham and the natural ." +\
    " \nno curve balls here , no sliders ." +\
    " \nevery pitch is predictable ." +\
    " \na blind umpire could call this movie ." +\
    " \nsummer catch is strictly rookie league moviemaking ." +\
    " \nit has as much chance of making the movie hall of fame as the dodgers have of moving back to brooklyn ." +\
    " \n"

# Amazon multiple domains corpus
text_2 = "The best and least expensive digital camera I've ever owned This camera has given me no problems." +\
    " The software that comes with it is great as well." +\
    " I highly recommend it!" +\
    " My friends from work have to buy for themselves too after seeing how this little machine works." +\
    " It gives good video (3 mins with awesome sound) unlike other expensive cameras that does not really capture good"

text_2a = "there was a huge crowd - so many over 100 people could not be admitted - at a premiere screening of \" the nephew \" ( first screening with a major general audience admittance ) ." +\
    "\nthis was a movie premiere at the santa barbara international film festival ." +\
    " \npierce brosnan ( 007 ) , produced his first movie with beau st . clair ." +\
    " \nit was a constantly mind-moving and personal movie with lovely scenes of ireland ." +\
    " \nchad ( hill harper , beloved ) is a cute 17 year old mixed race ( african american and irish ) nephew , who's irish mother died ." +\
    " \nhe comes \" back to ireland \" , living with the curmudgeon uncle , tony egan ( donal mccann ) ." +\
    " \nhe meets pierce brosnan's character , mr . o'brady ( or just brady ) , because he falls in love with the beautiful daughter ." +\
    " \nthere are many scenes ( ah , character scenes ) to laugh at , others pull some tears ." +\
    " \nthe three mentioned above were at the premiere in the flesh , with the director eugene brady ." +\
    " \nafter the movie they took questions ." +\
    " \nthe movie was very good , it not fantastic ." +\
    " \nthe nephew has not been \" picked up \" in north america but has been in the rest of the world ." +\
    " \nthe nephew is generation secrecy of a \" titanic \" proportion ." +\
    " \nlet's hope the rest of america will be able to see the nephew ." +\
    " \ncontact given in the program guide : \" print source : irish dream source , inc . , tel : ( 310 ) 449-3411 \" \n"

text_2b = "this is not a simple plan about finding a plane load of money and getting away with the cash ." +\
    " \nthis is more about a parable of greed , and how money can become the bane of your life ." +\
    " \nyes , there are elements of ? fargo' here ( the snow and cold ) , although not as vivid in the blood and gore department ." +\
    " \nit shows how greed can set of a chain of events leading to death and the destruction of lives ." +\
    " \nand how at the end of the day , the things that matter most are love , truth and honesty ." +\
    " \nalthough in one sense it may seem tedious , making a movie about the ugliness of greed ( not box office material ) , it does become tedious , not because of the morale ending , but because one expects the movie to end that way ." +\
    " \nthis becomes apparent after the first murder to cover up the crime , the rest of the movie just spirals downward from there ." +\
    " \nthe characters in this drama are a mixture of simple and intellectual folk , brothers and friends , who all fall prey to the avarice of money ." +\
    " \nthey should have perhaps thrown in someone sensible , level headed and not affected by greed to give the party more balance ." +\
    " \ncommendable is the exceptional performance of billy bob thornton , whose portrayal of the simpleton brother was masterful ." +\
    " \nbill paxton also gives a powerful performance as the greedier younger brother , whilst bridget fonda is convincing as the greediest wife , who indirectly causes the most problems ." +\
    " \nfill a room full of greedy people and several million dollars , and you will end up with a simple recipe for a blood bath ." +\
    " \nit's not a simple plan , when you shoot everyone you love for money , unless you're the menendez brothers . \n"


def test_split_into_sentences():
    expected_sentences_1 = 22
    expected_sentences_1a = 25
    expected_sentences_2 = 5
    assert len(pre.split_into_sentences(text_1)) == expected_sentences_1
    assert len(pre.split_into_sentences(text_1a)) == expected_sentences_1a
    assert len(pre.split_into_sentences(text_2)) == expected_sentences_2


def test_filter_irrealis_block():
    text_1_sentences = pre.split_into_sentences(text_1)
    filtered_senteces_1 = pre.filter_irrealis_block(text_1_sentences)
    expected_sentences_1 = 20

    text_1a_sentences = pre.split_into_sentences(text_1a)
    filtered_senteces_1a = pre.filter_irrealis_block(text_1a_sentences)
    expected_sentences_1a = 22

    text_2_sentences = pre.split_into_sentences(text_2)
    filtered_senteces_2 = pre.filter_irrealis_block(text_2_sentences)
    expected_sentences_2 = 5
    assert len(filtered_senteces_1) == expected_sentences_1
    assert len(filtered_senteces_1a) == expected_sentences_1a
    assert len(filtered_senteces_2) == expected_sentences_2


def test_turn_into_bag_of_words():

    bow_sentences = pre.start(text_2)
    assert len(bow_sentences[0]) == 7
    assert len(bow_sentences[1]) == 4
    assert len(bow_sentences[2]) == 1
    assert len(bow_sentences[3]) == 6
    assert len(bow_sentences[4]) == 9


def test_tag_negation():

    bow_sentences = pre.start(text_2)
    #due to negation
    expected_bigrams_counting = 5
    bigrams_counting = 0
    for s in bow_sentences:
        for ngram in s:
            if pre.is_bigram(ngram):
                bigrams_counting += 1
    assert expected_bigrams_counting == bigrams_counting


def test_tag_negation_a():
    bow_sentences = pre.start(text_2a)
    expected_bigrams_counting = 8
    bigrams_counting = 0
    for s in bow_sentences:
        for ngram in s:
            if pre.is_bigram(ngram):
                bigrams_counting += 1
    assert expected_bigrams_counting == bigrams_counting


def test_tag_negation_b():

    bow_sentences = pre.start(text_2b)
    expected_bigrams_counting = 11
    bigrams_counting = 0
    for s in bow_sentences:
        for ngram in s:
            if pre.is_bigram(ngram):
                bigrams_counting += 1
    assert expected_bigrams_counting == bigrams_counting
