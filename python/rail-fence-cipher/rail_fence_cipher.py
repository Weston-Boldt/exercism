class Rails:

    def __init__(self, message, num_rails):
        self.message = message
        self.num_rails = num_rails
        self.reset()
        self.rails = [[] for _ in range(self.num_rails)]
        self.build_rails()

    def build_rails(self):
        for data in self.message:
            self.rails[self.rails_index].append(data)
            self.increment_rails_index()

    def increment_rails_index(self):
        self.rails_index_reverse_direction()
        if self.rails_index_increasing:
            self.rails_index += 1
        else:
            self.rails_index -= 1

    def rails_index_reverse_direction(self):
        if self.rails_index == 0:
            self.rails_index_increasing = True
        elif self.rails_index == self.num_rails - 1:
            self.rails_index_increasing = False

    def reset(self):
        self.rails_index = 0
        self.rails_index_increasing = True


class RailsFenceCipher:

    def __init__(self, message, num_rails):
        self.message = message
        self.num_rails = num_rails
        self.rails = Rails(message, num_rails)

    def encode(self):
        return ''.join([data for rail in self.rails.rails for data in rail])

    def decode(self):
        output_message = list(self.message)
        output_rails = [[] for _ in range(self.num_rails)]
        rail_lengths = [len(rail) for rail in self.rails.rails]
        for index in xrange(len(output_rails)):
            for rail_length in xrange(rail_lengths[index]):
                output_rails[index].append(output_message.pop(0))
        original_message = ''.join([data for rail in output_rails for data in rail])
        temp_rails = Rails(original_message, self.num_rails)
        return ''.join([data for rail in temp_rails.rails for data in rail])


def encode(message, num_rails):
    return RailsFenceCipher(message, num_rails).encode()


def decode(message, num_rails):
    return RailsFenceCipher(message, num_rails).decode()
