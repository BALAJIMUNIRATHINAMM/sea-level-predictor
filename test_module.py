import unittest
from src.sea_level_predictor import draw_plot

class TestSeaLevelPredictor(unittest.TestCase):
    def test_plot_runs(self):
        """Test if the plot function runs without errors"""
        try:
            draw_plot()
            success = True
        except Exception as e:
            print(e)
            success = False
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()
