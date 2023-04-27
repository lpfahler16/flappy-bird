import nevopy as ne
from FlappyBirdModel import FlappyBirdModel
from multiprocessing import freeze_support
from joblib import dump


def fitness_function(genome):

    score = 0
    REPEATS = 100
    JUMP_FREQUENCY = 10

    for i in range(REPEATS):
        game = FlappyBirdModel()
        state = game.game_state()

        game_ended = False
        while(not game_ended):
            state = game.game_state()
            result = genome.process(game.game_state_evolve())
            if result[0] > result[1]:
                game.jump()

            for t in range(JUMP_FREQUENCY):
                game.tick()
                game_ended = game_ended or game.game_over()

        score += state['score']

    return score/REPEATS


if __name__ == '__main__':
    freeze_support()

    early_stopping_cb = ne.callbacks.FitnessEarlyStopping(
        fitness_threshold=30,
        min_consecutive_generations=3,
    )

    population = ne.neat.NeatPopulation(size=32,
                                        num_inputs=6,
                                        num_outputs=2)

    history = population.evolve(generations=50,
                                fitness_function=fitness_function,
                                callbacks=[early_stopping_cb])
    dump(population.fittest(), 'best_evolved_play.joblib')
    history.visualize()
