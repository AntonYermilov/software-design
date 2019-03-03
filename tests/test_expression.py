from tests import init_standard_env
from cli.expression import Expression, _Assignment, _Pipeline


def test_assignment_execution():
    env = init_standard_env()
    assignment = _Assignment(env, ['a', 'b'])
    assert isinstance(assignment, Expression)
    assert assignment.execute() == ''
    assert env.get_variable('a') == 'b'


def test_pipeline_execution():
    env = init_standard_env()
    pipeline = _Pipeline(env, [['echo', 'b']])
    assert isinstance(pipeline, Expression)
    assert pipeline.execute() == 'b\n'
