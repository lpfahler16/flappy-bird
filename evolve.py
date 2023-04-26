import nevopy as ne
from FlappyBirdModel import FlappyBirdModel
from multiprocessing import freeze_support
from joblib import dump

CONFIG = ne.neat.NeatConfig(
    weak_genomes_removal_pc=0.7,
    weight_mutation_chance=(0.7, 0.9),
    new_node_mutation_chance=(0.1, 0.5),
    new_connection_mutation_chance=(0.08, 0.5),
    enable_connection_mutation_chance=(0.08, 0.5),
    disable_inherited_connection_chance=0.75,
    mating_chance=0.75,
    interspecies_mating_chance=0.05,
    rank_prob_dist_coefficient=1.75,
    # weight mutation specifics
    weight_perturbation_pc=(0.05, 0.4),
    weight_reset_chance=(0.05, 0.4),
    new_weight_interval=(-2, 2),
    # mass extinction
    mass_extinction_threshold=25,
    maex_improvement_threshold_pc=0.03,
    # infanticide
    infanticide_output_nodes=True,
    infanticide_input_nodes=False,
    # speciation
    species_distance_threshold=1.75,
)


def fitness_function(genome):

    score = 0
    REPEATS = 20

    for i in range(REPEATS):
        game = FlappyBirdModel()
        state = game.game_state()

        while(not game.game_over()):
            game.tick()
            state = game.game_state()
            result = genome.process([state['birdY'], state['barrierX'],
                                    state['barrierY'], state['birdV']])

            if result[0] > result[1]:
                game.jump()

        score += state['score']

    return score/REPEATS


if __name__ == '__main__':
    freeze_support()
    population = ne.neat.NeatPopulation(size=100,
                                        num_inputs=4,
                                        num_outputs=2, config=CONFIG)

    history = population.evolve(generations=300,
                                fitness_function=fitness_function)
    dump(population.fittest(), 'best_evolved_play.joblib')
    history.visualize()
