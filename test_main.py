import os
from unittest import mock
import main

player = main.Player(player_name='player_name', lives=5, points=10, inventory=['water'])


def test_player_contains_items_for_true():
    item = 'water'
    assert player.contains_item(item=item) == True

def test_player_contains_items_for_false():
    item = 'boiler'
    assert player.contains_item(item=item) == False

def test_save_progress():
    main.save_progress(path_number=5, save_player=player)
    files_present = os.listdir(os.getcwd())
    assert 'progress.json' in files_present
    os.remove('progress.json')

@mock.patch('main.input', create=True)
@mock.patch('main.save_progress', create=True)
def test_play_save_progress(mock_save, mocked_input):
    mocked_input.side_effect = ['s']
    mock_save.return_value = "save"
    result = main.play(5, 'map', player)
    assert result == False

@mock.patch('main.input', create=True)
@mock.patch('main.save_progress', create=True)
def test_play_path_zero_true(mock_save, mocked_input):
    mocked_input.side_effect = ['x', 'solution']
    mock_save.return_value = "save"
    result = main.play(path_number=0, game_map=[main.Path(path_number=0, collectable_item=[], hint='hint',solution='solution')], player=player)
    assert result == True


@mock.patch('main.input', create=True)
@mock.patch('main.save_progress', create=True)
def test_play_path_one_True(mock_save, mocked_input):
    mocked_input.side_effect = ['x', 'u\nAxe', 'solution']
    mock_save.return_value = "save"
    player_1 = main.Player(player_name='player_name', lives=5, points=10, inventory=['Axe'])
    result = main.play(path_number=1, game_map=[None, main.Path(path_number=1, collectable_item=[], hint='hint',solution='solution')], player=player_1)
    assert result == True


@mock.patch('main.input', create=True)
@mock.patch('main.save_progress', create=True)
def test_play_path_two_True(mock_save, mocked_input):
    mocked_input.side_effect = ['x', 'u\nFlameThrower', 'solution']
    mock_save.return_value = "save"
    player = main.Player(player_name='player_name', lives=5, points=10, inventory=['FlameThrower'])
    result = main.play(2, [None, None, main.Path(path_number=0, collectable_item=[], hint='hint', solution='solution')], player)
    assert result == True


@mock.patch('main.input', create=True)
@mock.patch('main.save_progress', create=True)
def test_play_path_three_True(mock_save, mocked_input):
    mocked_input.side_effect = ['x', 'u\nTorch', 'solution']
    mock_save.return_value = "save"
    player = main.Player(player_name='player_name', lives=5, points=10, inventory=['Torch'])
    result = main.play(3, [None, None, None, main.Path(path_number=0, collectable_item=[], hint='hint', solution='solution')], player)
    assert result == True


@mock.patch('main.input', create=True)
@mock.patch('main.save_progress', create=True)
def test_play_path_four_True(mock_save, mocked_input):
    mocked_input.side_effect = ['x', 'Pick Map', 'solution']
    mock_save.return_value = "save"
    player = main.Player(player_name='player_name', lives=5, points=10, inventory=['Torch'])
    result = main.play(4, [None, None, None, None, main.Path(path_number=4, collectable_item=[], hint='hint', solution='solution')], player)
    assert result == True


@mock.patch('main.input', create=True)
@mock.patch('main.save_progress', create=True)
def test_play_path_zero_wrong_action(mock_save, mocked_input):
    mocked_input.side_effect = ['x', 'sol_2']
    mock_save.return_value = "save"
    result = main.play(0, [main.Path(path_number=0, collectable_item=[], hint='hint',solution=None)], player)
    assert result == False


@mock.patch('main.input', create=True)
@mock.patch('main.save_progress', create=True)
def test_play_path_one_wrong_action(mock_save, mocked_input):
    mocked_input.side_effect = ['x', 'u\nAxe', 'solution']
    mock_save.return_value = "save"
    player = main.Player(player_name='player_name', lives=5, points=10, inventory=['Axe'])
    result = main.play(1, [None, main.Path(path_number=1, collectable_item=[], hint='hint', solution=None)], player)
    assert result == False


@mock.patch('main.input', create=True)
@mock.patch('main.save_progress', create=True)
def test_play_path_two_wrong_action(mock_save, mocked_input):
    mocked_input.side_effect = ['x', 'u\nFlameThrower', 'solution']
    mock_save.return_value = "save"
    player = main.Player(player_name='player_name', lives=5, points=10, inventory=['FlameThrower'])
    result = main.play(2, [None, None, main.Path(path_number=2, collectable_item=[], hint='hint', solution=None)], player)
    assert result == False


@mock.patch('main.input', create=True)
@mock.patch('main.save_progress', create=True)
def test_play_path_three_wrong_action(mock_save, mocked_input):
    mocked_input.side_effect = ['x', 'u\nTorch', 'solution']
    mock_save.return_value = "save"
    player = main.Player(player_name='player_name', lives=5, points=10, inventory=['Torch'])
    result = main.play(3, [None, None, None, main.Path(path_number=3, collectable_item=[], hint='hint', solution=None)], player)
    assert result == False




@mock.patch('main.input', create=True)
@mock.patch('main.save_progress', create=True)
def test_play_path_four_wrong_action(mock_save, mocked_input):
    mocked_input.side_effect = ['x', 'Axe', 'solution']
    mock_save.return_value = "save"
    player = main.Player(player_name='player_name', lives=5, points=10, inventory=['Axe'])
    result = main.play(4, [None, None, None, None, main.Path(path_number=1, collectable_item=[], hint='hint', solution=None)], player)
    assert result == False


@mock.patch('main.input', create=True)
@mock.patch('main.save_progress', create=True)
def test_play_path_one_wrong_input(mock_save, mocked_input):
    mocked_input.side_effect = ['x', 'Axe', 'solution']
    mock_save.return_value = "save"
    player = main.Player(player_name='player_name', lives=5, points=10, inventory=['Axe'])
    result = main.play(1, [None, main.Path(path_number=1, collectable_item=[], hint='hint',solution=None)], player)
    assert result == False


@mock.patch('main.input', create=True)
@mock.patch('main.save_progress', create=True)
def test_play_path_two_wrong_input(mock_save, mocked_input):
    mocked_input.side_effect = ['x', 'Axe', 'solution']
    mock_save.return_value = "save"
    player = main.Player(player_name='player_name', lives=5, points=10, inventory=['Axe'])
    result = main.play(2, [None, None, main.Path(path_number=2, collectable_item=[], hint='hint',solution=None)], player)
    assert result == False


@mock.patch('main.input', create=True)
@mock.patch('main.save_progress', create=True)
def test_play_path_three_wrong_input(mock_save, mocked_input):
    mocked_input.side_effect = ['x', 'Axe', 'solution']
    mock_save.return_value = "save"
    player = main.Player(player_name='player_name', lives=5, points=10, inventory=['Axe'])
    result = main.play(3, [None, None, None, main.Path(path_number=3, collectable_item=[], hint='hint', solution=None)], player)
    assert result == False


@mock.patch('main.input', create=True)
@mock.patch('main.save_progress', create=True)
def test_play_path_wrong_input(mock_save, mocked_input):
    mocked_input.side_effect = ['x', 'Axe', 'solution']
    mock_save.return_value = "save"
    player = main.Player(player_name='player_name', lives=5, points=10, inventory=['Axe'])
    result = main.play(8, [None, None, None, main.Path(path_number=3, collectable_item=[], hint='hint', solution=None)], player)
    assert result == False



def test_load_map():
    result = main.load_map()
    assert type(result) == list

