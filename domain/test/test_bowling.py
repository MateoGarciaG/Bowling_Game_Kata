
from src.bowling import BowlingScoreCard
import pytest

def test_all_strikes():
    
    assert BowlingScoreCard("XXXXXXXXXXXX").total_score() == 300

def test_spare():
    
    assert BowlingScoreCard("5/5/5/5/5/5/5/5/5/5/5").total_score() == 150

def test_heartbreak():
    
    assert BowlingScoreCard("9-9-9-9-9-9-9-9-9-9-").total_score() == 90

def test_random_score():
    
    assert BowlingScoreCard("12345123451234512345").total_score() == 60
    assert BowlingScoreCard("81-92/X637-52X-62/X").total_score() == 122
    assert BowlingScoreCard("2345XX-98/-/187251").total_score() == 107
    assert BowlingScoreCard("18X7-2/819-XXX6/3").total_score() == 158
    assert BowlingScoreCard("X63--9/5281XX1/X8/").total_score() == 140
    assert BowlingScoreCard("-2XXX16427/634/XX6").total_score() == 154