from Slacktex.regex import textraction

class TestSlackBot:

    def setup(self):
        """Create a list of messages
        """
        self.messages = ['$\LaTeX$',
                        'What about some inline $\LaTeX$?',
                        '$i \hbar \slashed{\partial} \psi = mc \psi $',
                        '$\sum_{k=1}^{\aleph_0}\frac{1}{\frac{1}{\frac{1}{\frac{1}{\frac{1}{\frac{1}{\frac{1}{\frac{1}{1+k}}}}}}}}$',
                        '$exp(i \pi) + 1 = 0$',
                        'Come now, David, be a little more advanced: $\Box^2 A_\alpha = \mu J_\alpha$',
                        '$\nabla \cdot B = 0$ ... or it was 1?]',
                        '$$\sum dbl_{dollar}$$',
                        'A message\n over several lines\n with $\LaTeX$\n near the end']

        self.desired = ['\LaTeX',
                        '\LaTeX',
                        'i \hbar \slashed{\partial} \psi = mc \psi ',
                        '\sum_{k=1}^{\aleph_0}\frac{1}{\frac{1}{\frac{1}{\frac{1}{\frac{1}{\frac{1}{\frac{1}{\frac{1}{1+k}}}}}}}}',
                        'exp(i \pi) + 1 = 0',
                        '\Box^2 A_\alpha = \mu J_\alpha',
                        '\nabla \cdot B = 0',
                        '\sum dbl_{dollar}',
                        '\LaTeX']

    def test_textraction(self):
        for message, desired in zip(self.messages, self.desired):
            actual = textraction({'text':message})
            expected = desired
            assert actual == expected
