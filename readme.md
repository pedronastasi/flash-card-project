# Flash Card Project

This project is a flash card application that helps you learn French words. It displays a random French word and allows you to flip the card to see the English translation. You can mark whether you know the word or not, and the application will save the words you need to learn for future practice.

## Installation

1. Clone the repository: `git clone https://github.com/your-username/flash-card-project.git`
1. Navigate to the project directory: `cd flash-card-project`
1. Clone the repository or download the code files.
1. Create a new virtual environment. You can name it env or anything you like:

   ```Shell
      python -m venv env
   ```

   ```Shell
      .\env\Scripts\activate
   ```

   ```Shell
      source env/bin/activate
   ```

1. Install the required dependencies by running the following command in your terminal:
   ```shell
   pip install -r requirements.txt
   ```

## Usage

1. Run the application: `python main.py`
2. The application will display a French word.
3. Click the "Flip Card" button to see the English translation.
4. Click the "I Know It" button if you know the word, or the "I Don't Know It" button if you don't.
5. The application will save the words you need to learn in a CSV file for future practice.

## Customization

You can customize the application by modifying the following variables in the `main.py` file:

- `BACKGROUND_COLOR`: The background color of the application.
- `FONT_COLOR`: The font color of the text.
- `card_front_img`: The image file for the front side of the flash card.
- `card_back_img`: The image file for the back side of the flash card.
- `right_img`: The image file for the "I Know It" button.
- `wrong_img`: The image file for the "I Don't Know It" button.

## Data

The application uses a CSV file to store the French words and their English translations. By default, it looks for a file named `french_words.csv` in the `data` directory. If this file is not found, it falls back to a file named `words_to_learn.csv` in the same directory.

You can add your own words to the CSV file or replace it with your own file. Just make sure the file follows the same format: one column for the French words and another column for the English translations.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

