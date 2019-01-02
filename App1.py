{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "App1.ipynb",
      "version": "0.3.2",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "display_name": "Python [default]",
      "language": "python",
      "name": "python3"
    }
  },
  "cells": [
    {
      "metadata": {
        "id": "fXcRWRtz431v",
        "colab_type": "code",
        "outputId": "a5034806-8b2b-4cf0-e6b8-68361830ca64",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 17
        }
      },
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import plotly.offline as py\n",
        "py.init_notebook_mode(connected=True)\n",
        "import plotly.graph_objs as go\n",
        "import seaborn as sns\n",
        "from sklearn import metrics\n",
        "import random\n",
        "import os\n",
        "from sklearn.linear_model import LinearRegression\n",
        "%matplotlib inline"
      ],
      "execution_count": 62,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "<script>requirejs.config({paths: { 'plotly': ['https://cdn.plot.ly/plotly-latest.min']},});if(!window.Plotly) {{require(['plotly'],function(plotly) {window.Plotly=plotly;});}}</script>"
            ],
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "metadata": {
        "id": "nL5plfkk4-KO",
        "colab_type": "code",
        "outputId": "20b0d0f2-39c0-4fd8-f675-efedbaa7e69f",
        "colab": {
          "resources": {
            "http://localhost:8080/nbextensions/google.colab/files.js": {
              "data": "Ly8gQ29weXJpZ2h0IDIwMTcgR29vZ2xlIExMQwovLwovLyBMaWNlbnNlZCB1bmRlciB0aGUgQXBhY2hlIExpY2Vuc2UsIFZlcnNpb24gMi4wICh0aGUgIkxpY2Vuc2UiKTsKLy8geW91IG1heSBub3QgdXNlIHRoaXMgZmlsZSBleGNlcHQgaW4gY29tcGxpYW5jZSB3aXRoIHRoZSBMaWNlbnNlLgovLyBZb3UgbWF5IG9idGFpbiBhIGNvcHkgb2YgdGhlIExpY2Vuc2UgYXQKLy8KLy8gICAgICBodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvTElDRU5TRS0yLjAKLy8KLy8gVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yIGFncmVlZCB0byBpbiB3cml0aW5nLCBzb2Z0d2FyZQovLyBkaXN0cmlidXRlZCB1bmRlciB0aGUgTGljZW5zZSBpcyBkaXN0cmlidXRlZCBvbiBhbiAiQVMgSVMiIEJBU0lTLAovLyBXSVRIT1VUIFdBUlJBTlRJRVMgT1IgQ09ORElUSU9OUyBPRiBBTlkgS0lORCwgZWl0aGVyIGV4cHJlc3Mgb3IgaW1wbGllZC4KLy8gU2VlIHRoZSBMaWNlbnNlIGZvciB0aGUgc3BlY2lmaWMgbGFuZ3VhZ2UgZ292ZXJuaW5nIHBlcm1pc3Npb25zIGFuZAovLyBsaW1pdGF0aW9ucyB1bmRlciB0aGUgTGljZW5zZS4KCi8qKgogKiBAZmlsZW92ZXJ2aWV3IEhlbHBlcnMgZm9yIGdvb2dsZS5jb2xhYiBQeXRob24gbW9kdWxlLgogKi8KKGZ1bmN0aW9uKHNjb3BlKSB7CmZ1bmN0aW9uIHNwYW4odGV4dCwgc3R5bGVBdHRyaWJ1dGVzID0ge30pIHsKICBjb25zdCBlbGVtZW50ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnc3BhbicpOwogIGVsZW1lbnQudGV4dENvbnRlbnQgPSB0ZXh0OwogIGZvciAoY29uc3Qga2V5IG9mIE9iamVjdC5rZXlzKHN0eWxlQXR0cmlidXRlcykpIHsKICAgIGVsZW1lbnQuc3R5bGVba2V5XSA9IHN0eWxlQXR0cmlidXRlc1trZXldOwogIH0KICByZXR1cm4gZWxlbWVudDsKfQoKLy8gTWF4IG51bWJlciBvZiBieXRlcyB3aGljaCB3aWxsIGJlIHVwbG9hZGVkIGF0IGEgdGltZS4KY29uc3QgTUFYX1BBWUxPQURfU0laRSA9IDEwMCAqIDEwMjQ7Ci8vIE1heCBhbW91bnQgb2YgdGltZSB0byBibG9jayB3YWl0aW5nIGZvciB0aGUgdXNlci4KY29uc3QgRklMRV9DSEFOR0VfVElNRU9VVF9NUyA9IDMwICogMTAwMDsKCmZ1bmN0aW9uIF91cGxvYWRGaWxlcyhpbnB1dElkLCBvdXRwdXRJZCkgewogIGNvbnN0IHN0ZXBzID0gdXBsb2FkRmlsZXNTdGVwKGlucHV0SWQsIG91dHB1dElkKTsKICBjb25zdCBvdXRwdXRFbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQob3V0cHV0SWQpOwogIC8vIENhY2hlIHN0ZXBzIG9uIHRoZSBvdXRwdXRFbGVtZW50IHRvIG1ha2UgaXQgYXZhaWxhYmxlIGZvciB0aGUgbmV4dCBjYWxsCiAgLy8gdG8gdXBsb2FkRmlsZXNDb250aW51ZSBmcm9tIFB5dGhvbi4KICBvdXRwdXRFbGVtZW50LnN0ZXBzID0gc3RlcHM7CgogIHJldHVybiBfdXBsb2FkRmlsZXNDb250aW51ZShvdXRwdXRJZCk7Cn0KCi8vIFRoaXMgaXMgcm91Z2hseSBhbiBhc3luYyBnZW5lcmF0b3IgKG5vdCBzdXBwb3J0ZWQgaW4gdGhlIGJyb3dzZXIgeWV0KSwKLy8gd2hlcmUgdGhlcmUgYXJlIG11bHRpcGxlIGFzeW5jaHJvbm91cyBzdGVwcyBhbmQgdGhlIFB5dGhvbiBzaWRlIGlzIGdvaW5nCi8vIHRvIHBvbGwgZm9yIGNvbXBsZXRpb24gb2YgZWFjaCBzdGVwLgovLyBUaGlzIHVzZXMgYSBQcm9taXNlIHRvIGJsb2NrIHRoZSBweXRob24gc2lkZSBvbiBjb21wbGV0aW9uIG9mIGVhY2ggc3RlcCwKLy8gdGhlbiBwYXNzZXMgdGhlIHJlc3VsdCBvZiB0aGUgcHJldmlvdXMgc3RlcCBhcyB0aGUgaW5wdXQgdG8gdGhlIG5leHQgc3RlcC4KZnVuY3Rpb24gX3VwbG9hZEZpbGVzQ29udGludWUob3V0cHV0SWQpIHsKICBjb25zdCBvdXRwdXRFbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQob3V0cHV0SWQpOwogIGNvbnN0IHN0ZXBzID0gb3V0cHV0RWxlbWVudC5zdGVwczsKCiAgY29uc3QgbmV4dCA9IHN0ZXBzLm5leHQob3V0cHV0RWxlbWVudC5sYXN0UHJvbWlzZVZhbHVlKTsKICByZXR1cm4gUHJvbWlzZS5yZXNvbHZlKG5leHQudmFsdWUucHJvbWlzZSkudGhlbigodmFsdWUpID0+IHsKICAgIC8vIENhY2hlIHRoZSBsYXN0IHByb21pc2UgdmFsdWUgdG8gbWFrZSBpdCBhdmFpbGFibGUgdG8gdGhlIG5leHQKICAgIC8vIHN0ZXAgb2YgdGhlIGdlbmVyYXRvci4KICAgIG91dHB1dEVsZW1lbnQubGFzdFByb21pc2VWYWx1ZSA9IHZhbHVlOwogICAgcmV0dXJuIG5leHQudmFsdWUucmVzcG9uc2U7CiAgfSk7Cn0KCi8qKgogKiBHZW5lcmF0b3IgZnVuY3Rpb24gd2hpY2ggaXMgY2FsbGVkIGJldHdlZW4gZWFjaCBhc3luYyBzdGVwIG9mIHRoZSB1cGxvYWQKICogcHJvY2Vzcy4KICogQHBhcmFtIHtzdHJpbmd9IGlucHV0SWQgRWxlbWVudCBJRCBvZiB0aGUgaW5wdXQgZmlsZSBwaWNrZXIgZWxlbWVudC4KICogQHBhcmFtIHtzdHJpbmd9IG91dHB1dElkIEVsZW1lbnQgSUQgb2YgdGhlIG91dHB1dCBkaXNwbGF5LgogKiBAcmV0dXJuIHshSXRlcmFibGU8IU9iamVjdD59IEl0ZXJhYmxlIG9mIG5leHQgc3RlcHMuCiAqLwpmdW5jdGlvbiogdXBsb2FkRmlsZXNTdGVwKGlucHV0SWQsIG91dHB1dElkKSB7CiAgY29uc3QgaW5wdXRFbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoaW5wdXRJZCk7CiAgaW5wdXRFbGVtZW50LmRpc2FibGVkID0gZmFsc2U7CgogIGNvbnN0IG91dHB1dEVsZW1lbnQgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChvdXRwdXRJZCk7CiAgb3V0cHV0RWxlbWVudC5pbm5lckhUTUwgPSAnJzsKCiAgY29uc3QgcGlja2VkUHJvbWlzZSA9IG5ldyBQcm9taXNlKChyZXNvbHZlKSA9PiB7CiAgICBpbnB1dEVsZW1lbnQuYWRkRXZlbnRMaXN0ZW5lcignY2hhbmdlJywgKGUpID0+IHsKICAgICAgcmVzb2x2ZShlLnRhcmdldC5maWxlcyk7CiAgICB9KTsKICB9KTsKCiAgY29uc3QgY2FuY2VsID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnYnV0dG9uJyk7CiAgaW5wdXRFbGVtZW50LnBhcmVudEVsZW1lbnQuYXBwZW5kQ2hpbGQoY2FuY2VsKTsKICBjYW5jZWwudGV4dENvbnRlbnQgPSAnQ2FuY2VsIHVwbG9hZCc7CiAgY29uc3QgY2FuY2VsUHJvbWlzZSA9IG5ldyBQcm9taXNlKChyZXNvbHZlKSA9PiB7CiAgICBjYW5jZWwub25jbGljayA9ICgpID0+IHsKICAgICAgcmVzb2x2ZShudWxsKTsKICAgIH07CiAgfSk7CgogIC8vIENhbmNlbCB1cGxvYWQgaWYgdXNlciBoYXNuJ3QgcGlja2VkIGFueXRoaW5nIGluIHRpbWVvdXQuCiAgY29uc3QgdGltZW91dFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgc2V0VGltZW91dCgoKSA9PiB7CiAgICAgIHJlc29sdmUobnVsbCk7CiAgICB9LCBGSUxFX0NIQU5HRV9USU1FT1VUX01TKTsKICB9KTsKCiAgLy8gV2FpdCBmb3IgdGhlIHVzZXIgdG8gcGljayB0aGUgZmlsZXMuCiAgY29uc3QgZmlsZXMgPSB5aWVsZCB7CiAgICBwcm9taXNlOiBQcm9taXNlLnJhY2UoW3BpY2tlZFByb21pc2UsIHRpbWVvdXRQcm9taXNlLCBjYW5jZWxQcm9taXNlXSksCiAgICByZXNwb25zZTogewogICAgICBhY3Rpb246ICdzdGFydGluZycsCiAgICB9CiAgfTsKCiAgaWYgKCFmaWxlcykgewogICAgcmV0dXJuIHsKICAgICAgcmVzcG9uc2U6IHsKICAgICAgICBhY3Rpb246ICdjb21wbGV0ZScsCiAgICAgIH0KICAgIH07CiAgfQoKICBjYW5jZWwucmVtb3ZlKCk7CgogIC8vIERpc2FibGUgdGhlIGlucHV0IGVsZW1lbnQgc2luY2UgZnVydGhlciBwaWNrcyBhcmUgbm90IGFsbG93ZWQuCiAgaW5wdXRFbGVtZW50LmRpc2FibGVkID0gdHJ1ZTsKCiAgZm9yIChjb25zdCBmaWxlIG9mIGZpbGVzKSB7CiAgICBjb25zdCBsaSA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2xpJyk7CiAgICBsaS5hcHBlbmQoc3BhbihmaWxlLm5hbWUsIHtmb250V2VpZ2h0OiAnYm9sZCd9KSk7CiAgICBsaS5hcHBlbmQoc3BhbigKICAgICAgICBgKCR7ZmlsZS50eXBlIHx8ICduL2EnfSkgLSAke2ZpbGUuc2l6ZX0gYnl0ZXMsIGAgKwogICAgICAgIGBsYXN0IG1vZGlmaWVkOiAkewogICAgICAgICAgICBmaWxlLmxhc3RNb2RpZmllZERhdGUgPyBmaWxlLmxhc3RNb2RpZmllZERhdGUudG9Mb2NhbGVEYXRlU3RyaW5nKCkgOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAnbi9hJ30gLSBgKSk7CiAgICBjb25zdCBwZXJjZW50ID0gc3BhbignMCUgZG9uZScpOwogICAgbGkuYXBwZW5kQ2hpbGQocGVyY2VudCk7CgogICAgb3V0cHV0RWxlbWVudC5hcHBlbmRDaGlsZChsaSk7CgogICAgY29uc3QgZmlsZURhdGFQcm9taXNlID0gbmV3IFByb21pc2UoKHJlc29sdmUpID0+IHsKICAgICAgY29uc3QgcmVhZGVyID0gbmV3IEZpbGVSZWFkZXIoKTsKICAgICAgcmVhZGVyLm9ubG9hZCA9IChlKSA9PiB7CiAgICAgICAgcmVzb2x2ZShlLnRhcmdldC5yZXN1bHQpOwogICAgICB9OwogICAgICByZWFkZXIucmVhZEFzQXJyYXlCdWZmZXIoZmlsZSk7CiAgICB9KTsKICAgIC8vIFdhaXQgZm9yIHRoZSBkYXRhIHRvIGJlIHJlYWR5LgogICAgbGV0IGZpbGVEYXRhID0geWllbGQgewogICAgICBwcm9taXNlOiBmaWxlRGF0YVByb21pc2UsCiAgICAgIHJlc3BvbnNlOiB7CiAgICAgICAgYWN0aW9uOiAnY29udGludWUnLAogICAgICB9CiAgICB9OwoKICAgIC8vIFVzZSBhIGNodW5rZWQgc2VuZGluZyB0byBhdm9pZCBtZXNzYWdlIHNpemUgbGltaXRzLiBTZWUgYi82MjExNTY2MC4KICAgIGxldCBwb3NpdGlvbiA9IDA7CiAgICB3aGlsZSAocG9zaXRpb24gPCBmaWxlRGF0YS5ieXRlTGVuZ3RoKSB7CiAgICAgIGNvbnN0IGxlbmd0aCA9IE1hdGgubWluKGZpbGVEYXRhLmJ5dGVMZW5ndGggLSBwb3NpdGlvbiwgTUFYX1BBWUxPQURfU0laRSk7CiAgICAgIGNvbnN0IGNodW5rID0gbmV3IFVpbnQ4QXJyYXkoZmlsZURhdGEsIHBvc2l0aW9uLCBsZW5ndGgpOwogICAgICBwb3NpdGlvbiArPSBsZW5ndGg7CgogICAgICBjb25zdCBiYXNlNjQgPSBidG9hKFN0cmluZy5mcm9tQ2hhckNvZGUuYXBwbHkobnVsbCwgY2h1bmspKTsKICAgICAgeWllbGQgewogICAgICAgIHJlc3BvbnNlOiB7CiAgICAgICAgICBhY3Rpb246ICdhcHBlbmQnLAogICAgICAgICAgZmlsZTogZmlsZS5uYW1lLAogICAgICAgICAgZGF0YTogYmFzZTY0LAogICAgICAgIH0sCiAgICAgIH07CiAgICAgIHBlcmNlbnQudGV4dENvbnRlbnQgPQogICAgICAgICAgYCR7TWF0aC5yb3VuZCgocG9zaXRpb24gLyBmaWxlRGF0YS5ieXRlTGVuZ3RoKSAqIDEwMCl9JSBkb25lYDsKICAgIH0KICB9CgogIC8vIEFsbCBkb25lLgogIHlpZWxkIHsKICAgIHJlc3BvbnNlOiB7CiAgICAgIGFjdGlvbjogJ2NvbXBsZXRlJywKICAgIH0KICB9Owp9CgpzY29wZS5nb29nbGUgPSBzY29wZS5nb29nbGUgfHwge307CnNjb3BlLmdvb2dsZS5jb2xhYiA9IHNjb3BlLmdvb2dsZS5jb2xhYiB8fCB7fTsKc2NvcGUuZ29vZ2xlLmNvbGFiLl9maWxlcyA9IHsKICBfdXBsb2FkRmlsZXMsCiAgX3VwbG9hZEZpbGVzQ29udGludWUsCn07Cn0pKHNlbGYpOwo=",
              "ok": true,
              "headers": [
                [
                  "content-type",
                  "application/javascript"
                ]
              ],
              "status": 200,
              "status_text": ""
            }
          },
          "base_uri": "https://localhost:8080/",
          "height": 73
        }
      },
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "uploaded = files.upload()"
      ],
      "execution_count": 63,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-ed13ae33-20f7-4bd9-87b8-35f98ea1c72f\" name=\"files[]\" multiple disabled />\n",
              "     <output id=\"result-ed13ae33-20f7-4bd9-87b8-35f98ea1c72f\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script src=\"/nbextensions/google.colab/files.js\"></script> "
            ],
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "stream",
          "text": [
            "Saving googleplaystore.csv to googleplaystore (1).csv\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "Q3ArE_zC4319",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "df=pd.read_csv('googleplaystore.csv')"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "RT5Y4urS432C",
        "colab_type": "code",
        "outputId": "cf364572-98b4-4faa-cec8-9ea3fc193fe7",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 296
        }
      },
      "cell_type": "code",
      "source": [
        "df.head()"
      ],
      "execution_count": 65,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>App</th>\n",
              "      <th>Category</th>\n",
              "      <th>Rating</th>\n",
              "      <th>Reviews</th>\n",
              "      <th>Size</th>\n",
              "      <th>Installs</th>\n",
              "      <th>Type</th>\n",
              "      <th>Price</th>\n",
              "      <th>Content Rating</th>\n",
              "      <th>Genres</th>\n",
              "      <th>Last Updated</th>\n",
              "      <th>Current Ver</th>\n",
              "      <th>Android Ver</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Photo Editor &amp; Candy Camera &amp; Grid &amp; ScrapBook</td>\n",
              "      <td>ART_AND_DESIGN</td>\n",
              "      <td>4.1</td>\n",
              "      <td>159</td>\n",
              "      <td>19M</td>\n",
              "      <td>10,000+</td>\n",
              "      <td>Free</td>\n",
              "      <td>0</td>\n",
              "      <td>Everyone</td>\n",
              "      <td>Art &amp; Design</td>\n",
              "      <td>January 7, 2018</td>\n",
              "      <td>1.0.0</td>\n",
              "      <td>4.0.3 and up</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Coloring book moana</td>\n",
              "      <td>ART_AND_DESIGN</td>\n",
              "      <td>3.9</td>\n",
              "      <td>967</td>\n",
              "      <td>14M</td>\n",
              "      <td>500,000+</td>\n",
              "      <td>Free</td>\n",
              "      <td>0</td>\n",
              "      <td>Everyone</td>\n",
              "      <td>Art &amp; Design;Pretend Play</td>\n",
              "      <td>January 15, 2018</td>\n",
              "      <td>2.0.0</td>\n",
              "      <td>4.0.3 and up</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>U Launcher Lite – FREE Live Cool Themes, Hide ...</td>\n",
              "      <td>ART_AND_DESIGN</td>\n",
              "      <td>4.7</td>\n",
              "      <td>87510</td>\n",
              "      <td>8.7M</td>\n",
              "      <td>5,000,000+</td>\n",
              "      <td>Free</td>\n",
              "      <td>0</td>\n",
              "      <td>Everyone</td>\n",
              "      <td>Art &amp; Design</td>\n",
              "      <td>August 1, 2018</td>\n",
              "      <td>1.2.4</td>\n",
              "      <td>4.0.3 and up</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Sketch - Draw &amp; Paint</td>\n",
              "      <td>ART_AND_DESIGN</td>\n",
              "      <td>4.5</td>\n",
              "      <td>215644</td>\n",
              "      <td>25M</td>\n",
              "      <td>50,000,000+</td>\n",
              "      <td>Free</td>\n",
              "      <td>0</td>\n",
              "      <td>Teen</td>\n",
              "      <td>Art &amp; Design</td>\n",
              "      <td>June 8, 2018</td>\n",
              "      <td>Varies with device</td>\n",
              "      <td>4.2 and up</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Pixel Draw - Number Art Coloring Book</td>\n",
              "      <td>ART_AND_DESIGN</td>\n",
              "      <td>4.3</td>\n",
              "      <td>967</td>\n",
              "      <td>2.8M</td>\n",
              "      <td>100,000+</td>\n",
              "      <td>Free</td>\n",
              "      <td>0</td>\n",
              "      <td>Everyone</td>\n",
              "      <td>Art &amp; Design;Creativity</td>\n",
              "      <td>June 20, 2018</td>\n",
              "      <td>1.1</td>\n",
              "      <td>4.4 and up</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                                                 App        Category  Rating  \\\n",
              "0     Photo Editor & Candy Camera & Grid & ScrapBook  ART_AND_DESIGN     4.1   \n",
              "1                                Coloring book moana  ART_AND_DESIGN     3.9   \n",
              "2  U Launcher Lite – FREE Live Cool Themes, Hide ...  ART_AND_DESIGN     4.7   \n",
              "3                              Sketch - Draw & Paint  ART_AND_DESIGN     4.5   \n",
              "4              Pixel Draw - Number Art Coloring Book  ART_AND_DESIGN     4.3   \n",
              "\n",
              "  Reviews  Size     Installs  Type Price Content Rating  \\\n",
              "0     159   19M      10,000+  Free     0       Everyone   \n",
              "1     967   14M     500,000+  Free     0       Everyone   \n",
              "2   87510  8.7M   5,000,000+  Free     0       Everyone   \n",
              "3  215644   25M  50,000,000+  Free     0           Teen   \n",
              "4     967  2.8M     100,000+  Free     0       Everyone   \n",
              "\n",
              "                      Genres      Last Updated         Current Ver  \\\n",
              "0               Art & Design   January 7, 2018               1.0.0   \n",
              "1  Art & Design;Pretend Play  January 15, 2018               2.0.0   \n",
              "2               Art & Design    August 1, 2018               1.2.4   \n",
              "3               Art & Design      June 8, 2018  Varies with device   \n",
              "4    Art & Design;Creativity     June 20, 2018                 1.1   \n",
              "\n",
              "    Android Ver  \n",
              "0  4.0.3 and up  \n",
              "1  4.0.3 and up  \n",
              "2  4.0.3 and up  \n",
              "3    4.2 and up  \n",
              "4    4.4 and up  "
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 65
        }
      ]
    },
    {
      "metadata": {
        "id": "CjiAGTPm432I",
        "colab_type": "code",
        "outputId": "ecfbf242-b23b-4c38-9834-9142fa452d37",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "print(df.shape)"
      ],
      "execution_count": 66,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "(10841, 13)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "HltoLaoe432O",
        "colab_type": "code",
        "outputId": "892fad9f-0477-42e0-e8ba-159740198fd0",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 319
        }
      },
      "cell_type": "code",
      "source": [
        "df.info()"
      ],
      "execution_count": 67,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 10841 entries, 0 to 10840\n",
            "Data columns (total 13 columns):\n",
            "App               10841 non-null object\n",
            "Category          10841 non-null object\n",
            "Rating            9367 non-null float64\n",
            "Reviews           10841 non-null object\n",
            "Size              10841 non-null object\n",
            "Installs          10841 non-null object\n",
            "Type              10840 non-null object\n",
            "Price             10841 non-null object\n",
            "Content Rating    10840 non-null object\n",
            "Genres            10841 non-null object\n",
            "Last Updated      10841 non-null object\n",
            "Current Ver       10833 non-null object\n",
            "Android Ver       10838 non-null object\n",
            "dtypes: float64(1), object(12)\n",
            "memory usage: 1.1+ MB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "R2gfc2a6432W",
        "colab_type": "code",
        "outputId": "a27156e1-9118-405d-d1ea-a0ab82742980",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 252
        }
      },
      "cell_type": "code",
      "source": [
        "df.isnull().sum()"
      ],
      "execution_count": 68,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "App                  0\n",
              "Category             0\n",
              "Rating            1474\n",
              "Reviews              0\n",
              "Size                 0\n",
              "Installs             0\n",
              "Type                 1\n",
              "Price                0\n",
              "Content Rating       1\n",
              "Genres               0\n",
              "Last Updated         0\n",
              "Current Ver          8\n",
              "Android Ver          3\n",
              "dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 68
        }
      ]
    },
    {
      "metadata": {
        "id": "MASEFvWi432d",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "df.dropna(how = 'any',inplace = True)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "1jyCni_W432k",
        "colab_type": "code",
        "outputId": "5724f1cf-ca0e-4c09-900c-7681b80192bf",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 319
        }
      },
      "cell_type": "code",
      "source": [
        "df.info()"
      ],
      "execution_count": 70,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "Int64Index: 9360 entries, 0 to 10840\n",
            "Data columns (total 13 columns):\n",
            "App               9360 non-null object\n",
            "Category          9360 non-null object\n",
            "Rating            9360 non-null float64\n",
            "Reviews           9360 non-null object\n",
            "Size              9360 non-null object\n",
            "Installs          9360 non-null object\n",
            "Type              9360 non-null object\n",
            "Price             9360 non-null object\n",
            "Content Rating    9360 non-null object\n",
            "Genres            9360 non-null object\n",
            "Last Updated      9360 non-null object\n",
            "Current Ver       9360 non-null object\n",
            "Android Ver       9360 non-null object\n",
            "dtypes: float64(1), object(12)\n",
            "memory usage: 1023.8+ KB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "dRVZkDuy432q",
        "colab_type": "code",
        "outputId": "ce3fab82-8e9b-4ef1-b245-17b36fc26334",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "print(df.shape)"
      ],
      "execution_count": 71,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "(9360, 13)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "tg4K8Ujh432y",
        "colab_type": "code",
        "outputId": "33178aa1-84a7-42ec-a991-e31230866ebc",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 168
        }
      },
      "cell_type": "code",
      "source": [
        "df['Rating'].describe()"
      ],
      "execution_count": 72,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "count    9360.000000\n",
              "mean        4.191838\n",
              "std         0.515263\n",
              "min         1.000000\n",
              "25%         4.000000\n",
              "50%         4.300000\n",
              "75%         4.500000\n",
              "max         5.000000\n",
              "Name: Rating, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 72
        }
      ]
    },
    {
      "metadata": {
        "scrolled": false,
        "id": "aFAjpHdm4325",
        "colab_type": "code",
        "outputId": "20f88975-6cb1-45b3-d237-4ecac540c98d",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 514
        }
      },
      "cell_type": "code",
      "source": [
        "plt.figure(figsize = (11,8))\n",
        "sns.distplot(df['Rating'])"
      ],
      "execution_count": 73,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7feccf008b00>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 73
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\nusUcBdEAAAAASUVORK5CYII=\n",
            "text/plain": [
              "<matplotlib.figure.Figure at 0x7feccf008a90>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "metadata": {
        "id": "f_R17fI3433A",
        "colab_type": "code",
        "outputId": "5c29ab01-72af-422d-b240-3bfb16745a9f",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 168
        }
      },
      "cell_type": "code",
      "source": [
        "print(len(df['Category'].unique()),\"categories\")\n",
        "print(\"\\n\",df['Category'].unique())"
      ],
      "execution_count": 74,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "33 categories\n",
            "\n",
            " ['ART_AND_DESIGN' 'AUTO_AND_VEHICLES' 'BEAUTY' 'BOOKS_AND_REFERENCE'\n",
            " 'BUSINESS' 'COMICS' 'COMMUNICATION' 'DATING' 'EDUCATION' 'ENTERTAINMENT'\n",
            " 'EVENTS' 'FINANCE' 'FOOD_AND_DRINK' 'HEALTH_AND_FITNESS' 'HOUSE_AND_HOME'\n",
            " 'LIBRARIES_AND_DEMO' 'LIFESTYLE' 'GAME' 'FAMILY' 'MEDICAL' 'SOCIAL'\n",
            " 'SHOPPING' 'PHOTOGRAPHY' 'SPORTS' 'TRAVEL_AND_LOCAL' 'TOOLS'\n",
            " 'PERSONALIZATION' 'PRODUCTIVITY' 'PARENTING' 'WEATHER' 'VIDEO_PLAYERS'\n",
            " 'NEWS_AND_MAGAZINES' 'MAPS_AND_NAVIGATION']\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "ybK9P6yX433H",
        "colab_type": "code",
        "outputId": "3a359ee8-507e-457f-e2aa-78c15aae1b61",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        }
      },
      "cell_type": "code",
      "source": [
        "print(\"Skewness : %f\" % df['Rating'].skew())\n",
        "print(\"Kurtosis : %f\" % df['Rating'].kurt())"
      ],
      "execution_count": 75,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Skewness : -1.850135\n",
            "Kurtosis : 5.789216\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "scrolled": true,
        "id": "FserK5wj433P",
        "colab_type": "code",
        "outputId": "7205abdf-13a1-4523-cba5-749b17fc0562",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 483
        }
      },
      "cell_type": "code",
      "source": [
        "graph= sns.countplot(x=\"Category\",data=df, palette = \"Set1\")\n",
        "graph.set_xticklabels(graph.get_xticklabels(), rotation=90)\n",
        "graph "
      ],
      "execution_count": 76,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/seaborn/categorical.py:1428: FutureWarning:\n",
            "\n",
            "remove_na is deprecated and is a private function. Do not use.\n",
            "\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7feccef51978>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 76
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<matplotlib.figure.Figure at 0x7feccef30e48>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "metadata": {
        "id": "PwtvysxP433V",
        "colab_type": "code",
        "outputId": "0a1827b1-6b79-4df7-9902-d155b47953bc",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1058
        }
      },
      "cell_type": "code",
      "source": [
        "df.Size.value_counts()"
      ],
      "execution_count": 77,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Varies with device    1637\n",
              "14M                    165\n",
              "12M                    161\n",
              "15M                    159\n",
              "11M                    159\n",
              "13M                    157\n",
              "25M                    137\n",
              "17M                    131\n",
              "19M                    129\n",
              "21M                    120\n",
              "24M                    118\n",
              "16M                    117\n",
              "20M                    115\n",
              "26M                    110\n",
              "18M                    108\n",
              "23M                    106\n",
              "22M                     98\n",
              "10M                     96\n",
              "27M                     88\n",
              "28M                     77\n",
              "37M                     75\n",
              "33M                     71\n",
              "35M                     70\n",
              "30M                     69\n",
              "29M                     69\n",
              "31M                     66\n",
              "3.3M                    63\n",
              "40M                     58\n",
              "46M                     57\n",
              "44M                     57\n",
              "                      ... \n",
              "613k                     1\n",
              "865k                     1\n",
              "41k                      1\n",
              "540k                     1\n",
              "25k                      1\n",
              "454k                     1\n",
              "173k                     1\n",
              "683k                     1\n",
              "122k                     1\n",
              "780k                     1\n",
              "953k                     1\n",
              "78k                      1\n",
              "695k                     1\n",
              "721k                     1\n",
              "186k                     1\n",
              "720k                     1\n",
              "306k                     1\n",
              "208k                     1\n",
              "837k                     1\n",
              "45k                      1\n",
              "253k                     1\n",
              "903k                     1\n",
              "232k                     1\n",
              "20k                      1\n",
              "153k                     1\n",
              "460k                     1\n",
              "160k                     1\n",
              "219k                     1\n",
              "756k                     1\n",
              "655k                     1\n",
              "Name: Size, Length: 413, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 77
        }
      ]
    },
    {
      "metadata": {
        "id": "gJXFUxDN433Z",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "def SizeChange(size):\n",
        "  x=0\n",
        "  if 'M' in size:\n",
        "    x = size[:-1]\n",
        "    x = float(x)*1000000\n",
        "    return(x)\n",
        "  elif 'k' in size:\n",
        "    x = size[:-1]\n",
        "    x = float(x)*1000\n",
        "    return(x)\n",
        "  else:\n",
        "    return None\n",
        "\n",
        "df['Size'] = df['Size'].map(SizeChange)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "l-dR_ToS433e",
        "colab_type": "code",
        "outputId": "550bfb8b-f1ce-4ec9-a466-8805969915ec",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1058
        }
      },
      "cell_type": "code",
      "source": [
        "df.Size.value_counts()"
      ],
      "execution_count": 79,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "14000000.0    165\n",
              "12000000.0    161\n",
              "15000000.0    159\n",
              "11000000.0    159\n",
              "13000000.0    157\n",
              "25000000.0    137\n",
              "17000000.0    131\n",
              "19000000.0    129\n",
              "21000000.0    120\n",
              "24000000.0    118\n",
              "16000000.0    117\n",
              "20000000.0    115\n",
              "26000000.0    110\n",
              "18000000.0    108\n",
              "23000000.0    106\n",
              "10000000.0    102\n",
              "22000000.0     98\n",
              "27000000.0     88\n",
              "28000000.0     77\n",
              "37000000.0     75\n",
              "33000000.0     71\n",
              "35000000.0     70\n",
              "30000000.0     69\n",
              "29000000.0     69\n",
              "31000000.0     66\n",
              "3300000.0      63\n",
              "40000000.0     58\n",
              "44000000.0     57\n",
              "46000000.0     57\n",
              "48000000.0     56\n",
              "             ... \n",
              "862000.0        1\n",
              "780000.0        1\n",
              "308000.0        1\n",
              "24000.0         1\n",
              "240000.0        1\n",
              "72000.0         1\n",
              "176000.0        1\n",
              "714000.0        1\n",
              "61000.0         1\n",
              "203000.0        1\n",
              "730000.0        1\n",
              "861000.0        1\n",
              "81000.0         1\n",
              "779000.0        1\n",
              "373000.0        1\n",
              "283000.0        1\n",
              "175000.0        1\n",
              "414000.0        1\n",
              "78000.0         1\n",
              "746000.0        1\n",
              "582000.0        1\n",
              "840000.0        1\n",
              "713000.0        1\n",
              "170000.0        1\n",
              "811000.0        1\n",
              "676000.0        1\n",
              "430000.0        1\n",
              "647000.0        1\n",
              "778000.0        1\n",
              "598000.0        1\n",
              "Name: Size, Length: 411, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 79
        }
      ]
    },
    {
      "metadata": {
        "id": "uUT3zIV6433k",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "df.Size.fillna(method = 'ffill', inplace = True)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "B_3xhzTx433m",
        "colab_type": "code",
        "outputId": "e60c111e-b8c7-4aba-b617-53250e971c2f",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1058
        }
      },
      "cell_type": "code",
      "source": [
        "df.Size.value_counts()"
      ],
      "execution_count": 81,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "14000000.0    218\n",
              "11000000.0    197\n",
              "12000000.0    195\n",
              "13000000.0    194\n",
              "15000000.0    191\n",
              "25000000.0    174\n",
              "17000000.0    171\n",
              "19000000.0    160\n",
              "21000000.0    148\n",
              "24000000.0    145\n",
              "16000000.0    142\n",
              "18000000.0    140\n",
              "23000000.0    140\n",
              "26000000.0    134\n",
              "20000000.0    133\n",
              "22000000.0    128\n",
              "10000000.0    123\n",
              "27000000.0    116\n",
              "37000000.0    108\n",
              "28000000.0    102\n",
              "29000000.0     91\n",
              "30000000.0     89\n",
              "31000000.0     87\n",
              "35000000.0     85\n",
              "33000000.0     80\n",
              "44000000.0     75\n",
              "34000000.0     71\n",
              "3300000.0      70\n",
              "4000000.0      69\n",
              "48000000.0     68\n",
              "             ... \n",
              "175000.0        1\n",
              "780000.0        1\n",
              "308000.0        1\n",
              "24000.0         1\n",
              "240000.0        1\n",
              "176000.0        1\n",
              "714000.0        1\n",
              "61000.0         1\n",
              "203000.0        1\n",
              "730000.0        1\n",
              "861000.0        1\n",
              "81000.0         1\n",
              "496000.0        1\n",
              "283000.0        1\n",
              "414000.0        1\n",
              "50000.0         1\n",
              "78000.0         1\n",
              "746000.0        1\n",
              "582000.0        1\n",
              "840000.0        1\n",
              "713000.0        1\n",
              "170000.0        1\n",
              "811000.0        1\n",
              "676000.0        1\n",
              "430000.0        1\n",
              "647000.0        1\n",
              "778000.0        1\n",
              "373000.0        1\n",
              "696000.0        1\n",
              "598000.0        1\n",
              "Name: Size, Length: 411, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 81
        }
      ]
    },
    {
      "metadata": {
        "id": "Ql0KrHVG433q",
        "colab_type": "code",
        "outputId": "cd5c50b9-9e33-4c58-a54f-e33ce1666678",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 370
        }
      },
      "cell_type": "code",
      "source": [
        "print(len(df['Installs'].unique()),\"categories\")\n",
        "df['Installs'].value_counts()"
      ],
      "execution_count": 115,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "19 categories\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "12    1576\n",
              "14    1252\n",
              "10    1150\n",
              "8     1009\n",
              "13     752\n",
              "6      712\n",
              "11     537\n",
              "9      466\n",
              "7      431\n",
              "16     409\n",
              "4      309\n",
              "15     289\n",
              "5      201\n",
              "17      72\n",
              "2       69\n",
              "18      58\n",
              "3       56\n",
              "1        9\n",
              "0        3\n",
              "Name: Installs, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 115
        }
      ]
    },
    {
      "metadata": {
        "id": "7alfeSK-rCgx",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 84
        },
        "outputId": "8a473d39-b53c-4d56-d5cb-4fd8f6bf86d5"
      },
      "cell_type": "code",
      "source": [
        "df.Installs.unique()"
      ],
      "execution_count": 83,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['10,000+', '500,000+', '5,000,000+', '50,000,000+', '100,000+',\n",
              "       '50,000+', '1,000,000+', '10,000,000+', '5,000+', '100,000,000+',\n",
              "       '1,000,000,000+', '1,000+', '500,000,000+', '100+', '500+', '10+',\n",
              "       '5+', '50+', '1+'], dtype=object)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 83
        }
      ]
    },
    {
      "metadata": {
        "id": "lzSW-_pZ433v",
        "colab_type": "code",
        "outputId": "2a9b7777-a3e8-41a1-f063-fcf1395a72ad",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 118
        }
      },
      "cell_type": "code",
      "source": [
        "df.Installs.head()"
      ],
      "execution_count": 84,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0        10,000+\n",
              "1       500,000+\n",
              "2     5,000,000+\n",
              "3    50,000,000+\n",
              "4       100,000+\n",
              "Name: Installs, dtype: object"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 84
        }
      ]
    },
    {
      "metadata": {
        "id": "5-cEKuIc433x",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "df.Installs = df.Installs.apply(lambda x: x.replace(',',''))\n",
        "df.Installs = df.Installs.apply(lambda x: x.replace('+',''))\n",
        "df.Installs = df.Installs.apply(lambda x: int(x))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "fm2KeuGO4330",
        "colab_type": "code",
        "outputId": "2c2287cf-e783-4b67-beb2-ae0853817020",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 118
        }
      },
      "cell_type": "code",
      "source": [
        "df.Installs.head()"
      ],
      "execution_count": 86,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0       10000\n",
              "1      500000\n",
              "2     5000000\n",
              "3    50000000\n",
              "4      100000\n",
              "Name: Installs, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 86
        }
      ]
    },
    {
      "metadata": {
        "id": "ijO1CPvW4335",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "InstallsVal = sorted(list(df['Installs'].unique()))\n",
        "InstallsChange = {}\n",
        "for i in range(0,len(InstallsVal)):\n",
        "    InstallsChange[InstallsVal[i]]=i\n",
        "df['Installs'] = df['Installs'].map(InstallsChange).astype(int)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "00LehqpH4337",
        "colab_type": "code",
        "outputId": "964bb10f-80c6-465e-9db9-03d896125b7f",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 118
        }
      },
      "cell_type": "code",
      "source": [
        "df.Installs.head()"
      ],
      "execution_count": 117,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0     8\n",
              "1    11\n",
              "2    13\n",
              "3    15\n",
              "4    10\n",
              "Name: Installs, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 117
        }
      ]
    },
    {
      "metadata": {
        "id": "aQoQq21b433_",
        "colab_type": "code",
        "outputId": "1b61bdf0-bb2b-4686-e954-1822d942c945",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 202
        }
      },
      "cell_type": "code",
      "source": [
        "df.Price.unique()"
      ],
      "execution_count": 89,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['0', '$4.99', '$3.99', '$6.99', '$7.99', '$5.99', '$2.99', '$3.49',\n",
              "       '$1.99', '$9.99', '$7.49', '$0.99', '$9.00', '$5.49', '$10.00',\n",
              "       '$24.99', '$11.99', '$79.99', '$16.99', '$14.99', '$29.99',\n",
              "       '$12.99', '$2.49', '$10.99', '$1.50', '$19.99', '$15.99', '$33.99',\n",
              "       '$39.99', '$3.95', '$4.49', '$1.70', '$8.99', '$1.49', '$3.88',\n",
              "       '$399.99', '$17.99', '$400.00', '$3.02', '$1.76', '$4.84', '$4.77',\n",
              "       '$1.61', '$2.50', '$1.59', '$6.49', '$1.29', '$299.99', '$379.99',\n",
              "       '$37.99', '$18.99', '$389.99', '$8.49', '$1.75', '$14.00', '$2.00',\n",
              "       '$3.08', '$2.59', '$19.40', '$3.90', '$4.59', '$15.46', '$3.04',\n",
              "       '$13.99', '$4.29', '$3.28', '$4.60', '$1.00', '$2.95', '$2.90',\n",
              "       '$1.97', '$2.56', '$1.20'], dtype=object)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 89
        }
      ]
    },
    {
      "metadata": {
        "id": "WU7oK3Mj434D",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "df.Price=df.Price.apply(lambda x: x.replace('$',''))\n",
        "df.Price=df.Price.apply(lambda x: float(x))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "39H8E-cm434G",
        "colab_type": "code",
        "outputId": "b86ad9aa-fd08-498f-bebd-d5ae126d1b2d",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 185
        }
      },
      "cell_type": "code",
      "source": [
        "df.Price.unique()"
      ],
      "execution_count": 91,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([  0.  ,   4.99,   3.99,   6.99,   7.99,   5.99,   2.99,   3.49,\n",
              "         1.99,   9.99,   7.49,   0.99,   9.  ,   5.49,  10.  ,  24.99,\n",
              "        11.99,  79.99,  16.99,  14.99,  29.99,  12.99,   2.49,  10.99,\n",
              "         1.5 ,  19.99,  15.99,  33.99,  39.99,   3.95,   4.49,   1.7 ,\n",
              "         8.99,   1.49,   3.88, 399.99,  17.99, 400.  ,   3.02,   1.76,\n",
              "         4.84,   4.77,   1.61,   2.5 ,   1.59,   6.49,   1.29, 299.99,\n",
              "       379.99,  37.99,  18.99, 389.99,   8.49,   1.75,  14.  ,   2.  ,\n",
              "         3.08,   2.59,  19.4 ,   3.9 ,   4.59,  15.46,   3.04,  13.99,\n",
              "         4.29,   3.28,   4.6 ,   1.  ,   2.95,   2.9 ,   1.97,   2.56,\n",
              "         1.2 ])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 91
        }
      ]
    },
    {
      "metadata": {
        "id": "KoIXPSRW434L",
        "colab_type": "code",
        "outputId": "2c8f27ba-b043-4bc5-943c-ce42143fab7f",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 168
        }
      },
      "cell_type": "code",
      "source": [
        "df.Price.describe()"
      ],
      "execution_count": 92,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "count    9360.000000\n",
              "mean        0.961279\n",
              "std        15.821640\n",
              "min         0.000000\n",
              "25%         0.000000\n",
              "50%         0.000000\n",
              "75%         0.000000\n",
              "max       400.000000\n",
              "Name: Price, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 92
        }
      ]
    },
    {
      "metadata": {
        "id": "R3vA1RYR434O",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "def Types(type):\n",
        "    if type == 'Free':\n",
        "        return 0\n",
        "    else:\n",
        "        return 1\n",
        "df.Type=df.Type.map(Types)    "
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "qZLNG3SK434Q",
        "colab_type": "code",
        "outputId": "96cae783-f56f-426e-ead3-d33c12003dae",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "df.Type.unique()"
      ],
      "execution_count": 94,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([0, 1])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 94
        }
      ]
    },
    {
      "metadata": {
        "id": "E3VXZkiL434T",
        "colab_type": "code",
        "outputId": "d9c7e1a4-0ad5-4792-95a5-d4f4738ebaf0",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        }
      },
      "cell_type": "code",
      "source": [
        "\n",
        "df['Content Rating'].unique()"
      ],
      "execution_count": 95,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['Everyone', 'Teen', 'Everyone 10+', 'Mature 17+',\n",
              "       'Adults only 18+', 'Unrated'], dtype=object)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 95
        }
      ]
    },
    {
      "metadata": {
        "id": "dZv0LZVi434U",
        "colab_type": "code",
        "outputId": "1a90f281-bcc1-4753-9c98-1c0c397b8ff9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 134
        }
      },
      "cell_type": "code",
      "source": [
        "df['Content Rating'].value_counts()"
      ],
      "execution_count": 96,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Everyone           7414\n",
              "Teen               1084\n",
              "Mature 17+          461\n",
              "Everyone 10+        397\n",
              "Adults only 18+       3\n",
              "Unrated               1\n",
              "Name: Content Rating, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 96
        }
      ]
    },
    {
      "metadata": {
        "id": "8tRYIUXS434X",
        "colab_type": "code",
        "outputId": "444740bd-e038-46cb-fcb3-10c5b69dbd83",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 422
        }
      },
      "cell_type": "code",
      "source": [
        "graph= sns.countplot(x=\"Content Rating\",data=df, palette = \"Set1\")\n",
        "graph.set_xticklabels(graph.get_xticklabels(), rotation=90)\n",
        "graph "
      ],
      "execution_count": 97,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/seaborn/categorical.py:1428: FutureWarning:\n",
            "\n",
            "remove_na is deprecated and is a private function. Do not use.\n",
            "\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7fecd21b1eb8>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 97
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYgAAAFBCAYAAABtpDhaAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4yLCBo\ndHRwOi8vbWF0cGxvdGxpYi5vcmcvNQv5yAAAIABJREFUeJzt3XmcHVWd/vFPkwRliRCwNSEquD4K\n+HPGAZU9EEBQkZ9EEFnEgBuiAjPIoDIgOLjruDEyjCiLIAiDCqMBJqwBgcFxRHT0UQQzKvhLCyGG\nxQBJ//6oarjpVCfdpKuru+7zfr3ui3tP3eV7X0A/95xTdU5Pf38/ERERg63TdAERETE+JSAiIqJS\nAiIiIiolICIiolICIiIiKiUgIiKi0uSmCxhNfX1Lc85uRMQI9fZO7alqTw8iIiIqJSAiIqJSAiIi\nIiolICIiolICIiIiKiUgIiKiUgIiIiIqJSAiIqJSAiIiIiq16krqKgv3nt10CSO2+byrmy4hIiI9\niIiIqJaAiIiISgmIiIiolICIiIhKCYiIiKiUgIiIiEoJiIiIqFTbdRCSjgAO7WjaBtgB+CrQD/zU\n9pHlcz8I7F+2n2L7B5I2Ai4ANgIeBA6yfX9d9UZExMp6+vvr36VT0i7AAcCWwPG2b5N0AXAe8Evg\nEmA7ijBYAGwFnAg8bPszkt4FvND236/uc6q2HM2FchERqzfUlqNjdSX1ScBc4Abbt5VtlwO7AzOA\nebYfBfokLaQIktnA4R3P/fcxqjUiIhiDgJC0LfA74HFgccehRRThcB/QV9E+vaN9oC0iIsbIWPQg\n3gGcXdFe2aUZon2o565k2rT1mTx50kptC4fzwnGmt3dq0yVERIxJQMwC3k8xAb1pR/tM4J7ypiHa\npwNLOtpWa/Hih0el4Kb19S1tuoSI6CJD/Sit9TRXSZsBD9p+1PZjwC8l7Vge3g+4ArgGeL2kdcvn\nzwT+B7iK4swmgDnlcyMiYozU3YOYQTF/MOAY4F8krQPcans+gKR/BW6g6GUcaXuFpC8B35S0AHgA\nOKTmWiMiosOYnOY6VnKaa0TEyA11mmuupI6IiEoJiIiIqJSAiIiISgmIiIiolICIiIhKCYiIiKiU\ngIiIiEoJiIiIqJSAiIiISgmIiIiolICIiIhKCYiIiKiUgIiIiEoJiIiIqJSAiIiISgmIiIiolICI\n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\n",
            "text/plain": [
              "<matplotlib.figure.Figure at 0x7fecd35d7cf8>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "metadata": {
        "id": "YOEOLGhz434b",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "df.Reviews=df.Reviews.apply(lambda x: int(x))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "QMzBBa9K434d",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "CategoryVal = sorted(list(df['Category'].unique()))\n",
        "Count = len(CategoryVal)\n",
        "CategoryChange = {}\n",
        "for i in range(0,Count):\n",
        "    CategoryChange[CategoryVal[i]]=i\n",
        "df[\"Category_int\"] = df[\"Category\"].map(CategoryChange).astype(int)   "
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "XISnaE_0434g",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "ContentVal = sorted(list(df['Content Rating'].unique()))\n",
        "ContentChange = {}\n",
        "for i in range(0,len(ContentVal)):\n",
        "    ContentChange[ContentVal[i]] = i\n",
        "df['Content Rating'] = df['Content Rating'].map(ContentChange).astype(int)    "
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "4I_7DXxa434n",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "GenresVal = sorted(list(df['Genres'].unique()))\n",
        "GenresChange = {}\n",
        "for i in range(0,len(GenresVal)):\n",
        "    GenresChange[GenresVal[i]]=i\n",
        "df['Genres'] = df['Genres'].map(GenresChange).astype(int)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "_LMlHlRl434p",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "df.drop(['Last Updated','Current Ver','Android Ver','App'], axis = 1,inplace = True)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "e4SDDO31434r",
        "colab_type": "code",
        "outputId": "b4b6c838-bb72-446a-b170-7c4fb49a4b7c",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 269
        }
      },
      "cell_type": "code",
      "source": [
        "df.info()"
      ],
      "execution_count": 103,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "Int64Index: 9360 entries, 0 to 10840\n",
            "Data columns (total 10 columns):\n",
            "Category          9360 non-null object\n",
            "Rating            9360 non-null float64\n",
            "Reviews           9360 non-null int64\n",
            "Size              9360 non-null float64\n",
            "Installs          9360 non-null int64\n",
            "Type              9360 non-null int64\n",
            "Price             9360 non-null float64\n",
            "Content Rating    9360 non-null int64\n",
            "Genres            9360 non-null int64\n",
            "Category_int      9360 non-null int64\n",
            "dtypes: float64(3), int64(6), object(1)\n",
            "memory usage: 1.1+ MB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "scrolled": true,
        "id": "Y4u_4SuI434v",
        "colab_type": "code",
        "outputId": "f77333ec-de6e-4644-9682-5c099eaa0aed",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 195
        }
      },
      "cell_type": "code",
      "source": [
        "df.head()"
      ],
      "execution_count": 104,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Category</th>\n",
              "      <th>Rating</th>\n",
              "      <th>Reviews</th>\n",
              "      <th>Size</th>\n",
              "      <th>Installs</th>\n",
              "      <th>Type</th>\n",
              "      <th>Price</th>\n",
              "      <th>Content Rating</th>\n",
              "      <th>Genres</th>\n",
              "      <th>Category_int</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>ART_AND_DESIGN</td>\n",
              "      <td>4.1</td>\n",
              "      <td>159</td>\n",
              "      <td>19000000.0</td>\n",
              "      <td>8</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1</td>\n",
              "      <td>9</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>ART_AND_DESIGN</td>\n",
              "      <td>3.9</td>\n",
              "      <td>967</td>\n",
              "      <td>14000000.0</td>\n",
              "      <td>11</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1</td>\n",
              "      <td>11</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>ART_AND_DESIGN</td>\n",
              "      <td>4.7</td>\n",
              "      <td>87510</td>\n",
              "      <td>8700000.0</td>\n",
              "      <td>13</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1</td>\n",
              "      <td>9</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>ART_AND_DESIGN</td>\n",
              "      <td>4.5</td>\n",
              "      <td>215644</td>\n",
              "      <td>25000000.0</td>\n",
              "      <td>15</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>4</td>\n",
              "      <td>9</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>ART_AND_DESIGN</td>\n",
              "      <td>4.3</td>\n",
              "      <td>967</td>\n",
              "      <td>2800000.0</td>\n",
              "      <td>10</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1</td>\n",
              "      <td>10</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "         Category  Rating  Reviews        Size  Installs  Type  Price  \\\n",
              "0  ART_AND_DESIGN     4.1      159  19000000.0         8     0    0.0   \n",
              "1  ART_AND_DESIGN     3.9      967  14000000.0        11     0    0.0   \n",
              "2  ART_AND_DESIGN     4.7    87510   8700000.0        13     0    0.0   \n",
              "3  ART_AND_DESIGN     4.5   215644  25000000.0        15     0    0.0   \n",
              "4  ART_AND_DESIGN     4.3      967   2800000.0        10     0    0.0   \n",
              "\n",
              "   Content Rating  Genres  Category_int  \n",
              "0               1       9             0  \n",
              "1               1      11             0  \n",
              "2               1       9             0  \n",
              "3               4       9             0  \n",
              "4               1      10             0  "
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 104
        }
      ]
    },
    {
      "metadata": {
        "id": "ycHxChof434z",
        "colab_type": "code",
        "outputId": "4c5201f1-0be8-46d4-8534-bb3e9337fcb8",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 665
        }
      },
      "cell_type": "code",
      "source": [
        "corrMat = df[['Rating','Reviews','Size','Installs','Type','Price','Content Rating','Genres','Category_int']].corr()\n",
        "mask = np.array(corrMat)\n",
        "mask[np.tril_indices_from(mask)] = False\n",
        "plt.subplots(figsize=(20,10))\n",
        "plt.xticks(rotation=90)\n",
        "sns.heatmap(corrMat, mask=mask,vmax=0.8, square=True,annot=True)"
      ],
      "execution_count": 105,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7fecd20a7be0>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 105
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAuUAAAJ3CAYAAAAzlC+2AAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4yLCBo\ndHRwOi8vbWF0cGxvdGxpYi5vcmcvNQv5yAAAIABJREFUeJzs3Xl4VNX9x/F3EkBZQggQQEWgWjlW\noSpu7AjWau2u1LauuK91rTsIiBsKskoRRVGrttYqbj+tilIryiJuuB0V3AAVEtawk/D7IzECAiqG\nOxfyfj3PPJl7z70z3zMT9OQz557JWrNmDZIkSZIyJzvTBUiSJElVnYNySZIkKcMclEuSJEkZ5qBc\nkiRJyjAH5ZIkSVKGVct0AduCM7JaVLklbPrNmZbpEiRJqtIKCnKzMl3DlpL02Grkmo8z/lqalEuS\nJEkZ5qBckiRJyjCnr0iSJClVcjI+mSR5JuWSJElShpmUS5IkKVVysqpeVG5SLkmSJGWYSbkkSZJS\nxTnlkiRJkhJnUi5JkqRUcU65JEmSpMQ5KJckSZIyzOkrkiRJShUv9JQkSZKUOJNySZIkpYoXekqS\nJElKnEm5JEmSUsU55ZIkSZISZ1IuSZKkVHFOuSRJkqTEmZRLkiQpVapialwV+yxJkiSlikm5JEmS\nUsU55ZIkSZISZ1IuSZKkVHGdckmSJEmJc1C+ldpxz5b0+/C/HHT28ZkuRZIkqVLlZGUlekuDrXb6\nSgihBTANmFq+a7vy7TNjjCUbOL4Z0CTGODmEMBgYEmP8KKl6K1ONWjX547C+vDduQqZLkSRJUiXY\n2pPyGGM8qPzWDqgBHL2RY7sBB5SfdP7WOiAHWL1iJcMP78HC2XMyXYokSZIqwVablG/EJGC3EMLN\nlA3AtwdGAo8AfYBVIYRPgQuBc4DuQB4QgF2B82OMT4YQLgX+DMwAqgMDY4zjk+3KxpWWlFBa8o0P\nAyRJkrYJXui5FQshVAd+C7wDfBxj7Ah0Aq6OMc4FxlA2ZeXR9U7dOcZ4OHAecHoIoT5lA/Z2wJlA\nl4S6IEmSpCpqa0/KQwhhfPn9nwL9Y4z/CCH0CSG8BKwECr7lMV4s/zmTstT8x8C0GOMyYFkIYfIW\nqFuSJEkbkZaLL5O0tSflFXPKgeeA90MIXSibP96lfP+Kb3mM1Wvdzyq/la61b03llStJkiR909ae\nlK/tYuAp4GrgsxjjqhDCb4CcEEINygba36W/HwOtyqfD1AP220L1brZmbVrRfWBPGrRoSsmqVbTp\nfjgjjzidpfMXZro0SZKkH6wqzinfZgblMcaPQgj/pmwQvVsI4b/AWOBx4G/AP4C7Qghzv+Vxvgwh\n3AdMBt4t/5mqqyo/ffUtbu76p0yXIUmSpEqy1Q7KY4wfs16KHWO8YgOHDlrr/o7lP+8t//nWWue+\nBRxUvvk+Zau1rKZs7fOtdvlESZKkrU1VnFO+1Q7Kt7AmlC2vuAK4N8Y4M8P1SJIkaRvmoHwDYow3\nADdkug5JkqSqqCrOKd/aV1+RJEmStnom5ZIkSUoVk3JJkiRJiTMplyRJUqpUxdVXTMolSZKkDDMp\nlyRJUqo4p1ySJElS4hyUS5IkSRnm9BVJkiSlihd6SpIkSUqcSbkkSZJSxQs9JUmSJCXOpFySJEmp\n4pxySZIkSYkzKZckSVKqOKdckiRJUuJMyiVJkpQqzimXJEmSlDiTckmSJKVKtkm5JEmSpKSZlEuS\nJClVsqrg8ism5ZIkSVKGmZRrs/Rq1DrTJSSq35xpmS5BkqQqI7sKJuUOyivB0LkvZrqERJ1b0DHT\nJUiSJG1TnL4iSZIkZZhJuSRJklIlK6fq5cZVr8eSJElSypiUS5IkKVXStiRiCGEQ0BZYA5wXY5yy\nVtvOwP1ADeDVGOMZm/McJuWSJEnSRoQQugC7xRjbAScDQ9c7ZCAwMMZ4AFASQmi2Oc9jUi5JkqRU\nSdmSiAcDYwFijO+GEPJDCHVjjItCCNlAJ+DP5e1nb+6TmJRLkiRJG9cEmLvW9tzyfQAFwGJgUAjh\nxRDC9Zv7JA7KJUmSlCpZ2dmJ3r5veevd3wkYAnQB9gkh/HJz+uygXJIkSdq42XydjAPsCHxefr8Q\n+CTGOD3GWAKMA/bcnCdxUC5JkqRUyc7JSvT2LZ4GugOEENoAs2OMiwFijKuBGSGE3cqP3ReIm9Nn\nL/SUJEmSNiLG+FIIYWoI4SWgFDg7hNADWBhjfBg4HxhTftHnNOCxzXkeB+WSJElKlbStUx5jvGy9\nXW+s1fYh0PGHPofTVyRJkqQMMymXJElSqmTlVL3cuOr1WJIkSUoZk3JJkiSlSsq+0TMRJuWSJElS\nhjkolyRJkjLM6SuSJElKlaxsp69IkiRJSphJuSRJklIl2yURJUmSJCXNpFySJEmpkuWSiJIkSZKS\nZlIuSZKkVKmKSbmD8pTpP2QEb779DllZWVx2/tm0+snuFW0vT5nK0FtHk52dTad2B3LGiccB8Ph/\nnuXO+/5JTk4O55zSg87t2/LK628y9NbRVMvJoWbN7bmu1+Xk1c3NVLd+sB33bMmZj9zGuEGjGX/L\n3ZkuR5IkqVKlclAeQmgBTAOmlu/arnz7zBhjyXd8jB7Awhjjw1uixi1hymtv8OnMmdw7ajgzPv6E\nXtfdxL2jhle03zB4OLfe3J9GBQ058ewLOOSgTjSon8/IO+/mn6NHsnTZMm4ZfRed27flpqF/44be\nV/Cj5jtz21338q9HHueU4/6cwd5tvhq1avLHYX15b9yETJciSZISUBVXX0nloLxcjDEe9NVGCGEM\ncDRwz3c8ecwWqWoLmvTKq3Tr1AGAXVo0Z9HiYoqXLKFO7dp8Nms2eXXr0qRxIwA6tTuQia+8RoP8\nerTdb19q165F7dq16HPphQDk18tj4aJFACxaXEyLZk0z06lKsHrFSoYf3oNDLz0z06VIkiRtEWke\nlK9vErBbCOFsygbnpcBYYDAwAwgxxuUhhC7AecCbQGGMcXgI4VqgE5ADDAemAMNijL8IIbQH/g+o\nT9mFr68DhwN/B0ooe42OjTF+sqU7WDhvPnvs3rJiu369PAqL5lGndm2K5s0nv17e12359fhs1myW\nr1jOsuXL+cslPVm0eDFnnnwCbfdrwyXnnsmJZ19I3dw61M3N5bwzTtnS5W8xpSUllJZ8pw9IJEnS\nNqAqzinfKj4bCCFUB34LzAe6Ax2BzsCRwE7As8DB5Yf/FnhwrXM7Ac1jjJ2BbkBPYBbQNISQBXQA\nXgP2BPYGJpc/xzMxxq6UDfB32MJd3KA1m2pbs6b8JyxctIhB1/Xlmisvpdd1N7FmzRquGzScwdf3\n5bF/3MU+e7Xinw8/kkzRkiRJ+t7SnJSHEML48vs/BfoDs4HdgOfL9+cCLYCHgF8DTwCHAr2Bi8qP\naQ+0XeuxsikbZE8DWgIHACOAdkBNYDzwKvBwCKEe8GCM8eUt0L9vaNSwAYVF8yq25xQWUdCgAQAF\nG2pr2JCaNbdn71Z7Uq1aDjs33ZHaNWsyb8ECPvhwBvv8tBUA7fbflyeeHpdEFyRJkn6w7GyT8jSJ\nMcaDyueVPwe8D6wEnvhqf4yxdYzxBcqS8s4hhNbA9Bjj4rUeZyUweq1zfhJjnEHZ4LstUIuyQX5b\nylLz52OMbwF7Af8Drg8hHJ9Eh9sfsB/PPP8CAO/E92nUsAG1a9cCYKcdmrBkyVJmff4Fq1eX8N8J\nE2l/wL60P2BfJk19jdLSUhYsXMjSZcvIz8ujQYN8pn/0MQBvvRtp1nSnJLogSZKkzZDmpHxtFwNP\nAYcA/UMItYBllM0nvyzGuCyE8Eb5cQ+ud+4kYEAIoT9QA7gpxvgX4L/ALcDbMcbCEEIBUCfG+FkI\n4U/AjBjj2BBCIXAUsMXX4du79Z7ssXtLjj39L2RnZ3Plhecy9omnyK1Th4O7dKTnxedzSe9rADjs\n4INo0WxnAA7p2pljTjsHgMsvKDv3qosvoE//m6lWrRp5ublcfcXFW7r8LaZZm1Z0H9iTBi2aUrJq\nFW26H87II05n6fyFmS5NkiRtAVmuvpJOMcaPQgj/Bs6gbCD+AmUXYY6NMS4rP+wh4C7g3PXOfSmE\n8DzwMpBF2VQVYowxhLAHcHv5ofOBL8rvvw+MDCEUlz/POo+5JV1w5qnrbIfddq24v9/eP11nicSv\nHPW7X3PU7369zr69W+/JPSOHbpkiE/bpq29xc9c/ZboMSZKkLSbrqwsGtflWFs6sUi/iuQUdM11C\n4vrNmZbpEiRJWkdBQe42O/F66q8PSXRste9jz2T8tdwqknJJkiRVHdkuiShJkiQpaSblkiRJShW/\nPEiSJElS4kzKJUmSlCpVcUnEqtdjSZIkKWVMyiVJkpQqrr4iSZIkKXEm5ZIkSUqVrGyTckmSJEkJ\nMymXJElSqmS7+ookSZKkpJmUS5IkKVX8Rk9JkiRJiTMplyRJUqr4jZ6SJEmSEmdSLkmSpFTJyq56\nuXHV67EkSZKUMg7KJUmSpAxz+ookSZJSxS8PkiRJkpQ4k3JJkiSliksiSpIkSUqcSbkkSZJSpSom\n5Q7Kpe+gV6PWmS4hcf3mTMt0CZIkVRkOyitBVsmqTJeQqBHTH8x0CYk6a9fumS5BkqQqxS8PkiRJ\nkpQ4k3JJkiSlSlZOTqZLSJxJuSRJkpRhJuWSJElKlaq4+krV67EkSZKUMiblkiRJSpVsV1+RJEmS\nlDSTckmSJKWKc8olSZIkJc5BuSRJkpRhTl+RJElSqjh9RZIkSVLiTMolSZKUKlkuiShJkiQpaSbl\nkiRJShXnlEuSJElKnEm5JEmSUsWkXJIkSVLiTMolSZKUKtkm5ZIkSZKSZlIuSZKkVHGdckmSJEmJ\n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\ngk08Uzrs3WIH9mjaiOOH/5vsrCwu/31nHpnyLrnbb0e7sDOPT32PTwsX8NDkdwD4xT4t6d52T3o/\n8Bwn/+1hVpeU0vPIgzLbie9pc/p8xAF7UFoKxwz9F9tVy+G6ow/JcC8qR7M2reg+sCcNWjSlZNUq\n2nQ/nJFHnM7S+QszXZokKQOytqKQrbJkbW3zUUMILYAHgbeAB2OMj4cQfgV0By4A7qfsIs4SYFiM\n8d8hhHFALmXzyB8F5gJ3AOcBjwPdgHPKH6OwfN/fKUviS4HeMcaNrrdX8tm0retF/IFWvvZ8pkvQ\nFnbBb2/OdAmJ6zdnWqZLkKTvpaAgd5v9qLT0/QmJjq2yW3bI+Gu51Q3K08hBubY1DsolKf0clFee\nNAzKt6npK5IkSdoGeKGnJEmSpKSZlEuSJCldsqpeblz1eixJkiSljEm5JEmS0sWkXJIkSVLSTMol\nSZKUKmtMyiVJkiQlzaRckiRJ6WJSLkmSJClpJuWSJElKl6yMf+t94kzKJUmSpAwzKZckSVK6ZFe9\n3Ljq9ViSJElKGZNySZIkpYrrlEuSJElKnINySZIkKcOcviJJkqR0cfqKJEmSpKSZlEuSJCldTMol\nSZIkJc2kXJIkSeliUi5JkiQpaSblkiRJSpWq+OVBDsolCejVqHWmS0hUvznTMl2CJGktDsorQUnd\nHTJdQqKWdT0l0yUkKic7K9MlJK7D1CMyXUKiJuzbMdMlSJLWVgWT8qrXY0mSJCllTMolSZKULllV\n71Nqk3JJkiQpw0zKJUmSlC7OKZckSZKUNJNySZIkpUpVXKe86vVYkiRJShkH5ZIkSVKGOX1FkiRJ\n6ZJd9XLjqtdjSZIkKWVMyiVJkpQuXugpSZIkKWkm5ZIkSUoXk3JJkiRJSTMplyRJUrqYlEuSJElK\nmkm5JEmSUmWNSbkkSZKkpJmUS5IkKV1MyiVJkiQlzaRckiRJ6ZKVlekKEmdSLkmSJGWYSbkkSZLS\nxTnlkiRJkpJmUp5i/W8ewptvvU1WVhaXXXQ+rfb4SUXby5OnMHTErWRnZ9OpQzvOOPnEirbly1fw\n+z8fy+kn9+B3v/plBir/fiZPmsjIW4aTk5NNuw4dOemU09ZpLy5eTO8rr6C4uJiatWrR95rryMvL\nq2gfMXwob735JiNG3c7y5cvo16c38+YVsXLFSk485VQ6duqcdJe+s8mTJjJi+DCys3Po0LEjJ5+6\n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\nKYZfcDx5ayXnklTVlKxZk+gtDbK+7ePkrU35dJUHY4z7rbd/TPn+x0MIPYBWwHBgLLAfZVNcRgLn\nAc8CewPLgMHAZTHGZRt7zsVLl1Xai/jq1KkMGzIEgG4/O5jjjj+BwsJCbh35N67s2YulS5fS68or\nWLhwIbm5ufS75lqqVatG1y6daf3Tn1Y8zmG/+AUAo0beSrPmXw9Gr+53DU122OEH1ZiTlfWDzgeY\nOnUqQ4YMBuBnB/+M408o6+fIv42gZ6+rWLp0KVdecQULFy4gNzeXa669jtzc3A2eV1paSp/evZkx\nYzo1ttuO6667niZNmvD6668zeNAgqlWrRl5eXfr06UvuZiyJWNn/WCvzPT70sF/Q84rLWbx4MatW\nreLU006nY6dOP7jGZasq76qX11+dysjhQwHo0u1g/nzs8RQVFnLHbSO5+PKeLF26lH5X9WTRwgXU\nyc2l19XXUKdOLjM/+5Trru7DmtJSdvnxj7no0it4/JGHueO2W9m5WfOKx+/Z52oaN/lhv9P13nnq\nB52/MYMeeIqp739MdlYWVx73G979ZDa5tbanfavd6HB2P/ba9et/m4e32wuAv40dR/PGDSv2X3fa\nH9ihQb1vPPYPcW77xC6VqdCsTSu6D+xJgxZNKVm1igWzvmTkEaezdH5yFyz3mzMtseeSklBQkPvD\n/4ecUhM/mZfoALVt8/oZfy2r9KA8xvjX8gs5j6RsqssVMcbnQwhnASdRlqSPjTFev6nnrMxB+dag\nMgblW5O0/AWdpMoclG8NttSgPK0yMShPAwfl2tZsy4Pylz4uSvR/vu1bNMj4a7nNDcozwUH5ts1B\n+bbPQXnV4KBc2xoH5ZUnDYPybXVOuSRJkrTV2FZXX5EkSdJWKi1f6JMkk3JJkiQpw0zKJUmSlCpp\n+UKfJJmUS5IkSRlmUi5JkqRUqYorn5mUS5IkSRlmUi5JkqRUKa16QblJuSRJkpRpJuWSJElKlZIq\nGJWblEuSJEkZZlIuSZKkVHGdckmSJEmJMymXJElSqpRUvaDcpFySJEnKNJNySZIkpYpzyiVJkiQl\nzkG5JEmSlGFOX5EkSVKq+OVBkiRJkhJnUi5JkqRU8UJPSZIkSYkzKZckSVKq+OVBkiRJkhJnUi5J\nqhJ6NWqd6RIS1W/OtEyXIG22qjin3EF5JahRujLTJSQqe9nCTJeQqO3nf5bpEhJXq0btTJeQqAWt\n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\n",
            "text/plain": [
              "<matplotlib.figure.Figure at 0x7fecd2118208>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "metadata": {
        "id": "fXREAgwq4342",
        "colab_type": "code",
        "outputId": "38438620-4153-4b8f-fac7-4dfcc61fd170",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 2148
        }
      },
      "cell_type": "code",
      "source": [
        "var = ['Reviews','Size','Rating','Type','Price','Content Rating','Genres','Category_int']\n",
        "for index in range(8):\n",
        "    data = pd.concat([df['Installs'],df[var[index]]],axis=1)\n",
        "    data.plot.scatter(x=var[index],y='Installs',ylim=(0,18),figsize=(6,4))"
      ],
      "execution_count": 118,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<matplotlib.figure.Figure at 0x7fecd2068940>"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n7gPWKaW+NYi2PnjJGYMwKwwYE4hFTEx/jbSOedOrT+qfseMY04BMMkIsYjKWiXPlxTtaitG560F1\n/tkPt06UUz5iGYzEDWIRk3jAP9YdO6ax0J5lwkjSIh41GUmYRGpveN1ZvyrO5rUZtm8crcdlBcxu\nbzjzxHodw2PYqgXkvSf97tGYVb2HU3Gj7qvl6vtMMtLQp871Vlxx4dZggQRk4No7Sql9uOb0Xdef\nHtScvoPodax8whYvSMxhYVDaO4NcvXM2cAOwGSgqpd4B/LLW+uVBtSkIgiC0ZpBf5P4QeGOL9zcP\nqm1BEAShObIjVxAEIURI0hcEQQgRkvQFQRBChCR9QRCEEDHszVlDQbR3BKiu5X7nL2zhH/716Y60\nWAwgGjEplyoEkIxpoK5V42krHTcplqFSruA+CjhigGmZGNjMBzg72Tlj2K1DE7UMTlufYa5oEzFt\nnjg0jV2L47T1I5QqBrlskj27t9XPWn3o8XE+8cWH6uU+eMkZ7Nyc499/8lP+8iuP1NtLxU1K5eq6\n+7xLQGfz2hHAIBm3OPDsZFUnx4Btp2SZnS83XHf7Z2Lz5OHpuh1Hq4ZKhYKrv7asTWNjgl3m6RcW\nNmkmo1C2q+c95+erFVrF6TCdL3Db3QcYn5xlbCSOjc3kdMG3vLdOoVji0Euzi8YtHrOYzhfr2kNO\n/LZt88wLC3E6/eVuz23fG2cqblGu2KTiUfZetou1Y+l2t0ZgVuQZuaK9IwiLOWf7Gq58+05g8WfE\nAG6+9nzec909S+JbP3HH6fDpOx/mB4++GLh8uzr98C+o/bFMnBuuPrejNkJ3Rq4kfEFYzPjkwpOq\n9zOykj4z7jhbXWv3Xqs6veDYDWp/ZrbY1/ZXZNLv4y5+QVgx5LLJ+s/ez8hK+sy442x1rd17rer0\ngmM3qP10MtrX9q19+/b11WA/yecL+7qpd9qGEe59uP9/lgnHFwbwrgu2oJ85Wp9nDzKbaVDVT6Fi\nd/wEbNY05b1tpeMmhmFg2DburxUiRvUMgYgV7PuGZMzEMg2SMYOKXf3+IGoZbNswykgqxomjMSam\nCvU4Tl8/wmg6ztYNWfbs3kYsWhXCOW3DCPfVPiPOnP6abJr1uQT/59Ej9fZSNb/jUbNBe3/z2hGy\nI3HWrU4xcWyuPqe9fVOWkWS04brbv1Uu/6A6p29ZJpZhN+j1b1mbJjuSIJuOMDmz8KSbjIJpmiSi\n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\n",
            "text/plain": [
              "<matplotlib.figure.Figure at 0x7feccf3f2828>"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAX0AAAEKCAYAAAD+XoUoAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4yLCBo\ndHRwOi8vbWF0cGxvdGxpYi5vcmcvNQv5yAAAIABJREFUeJztnXuYXFWZ7n9NX9LpTmK30IQgmSRC\nWEEChEPwQOSmJwxyGw6IZwgXEbyiqMAIjoyDYYZHc8L1ACpyGKMiEkZGxQucqLQCihFlggSQRUCC\nQW7J0A2hO+l0N33+qNve1V1rVfWuvau69/t7njxPf7X2t9a7V+36smvXXu9uGBkZQQghRDrYqdYC\nhBBCJIeKvhBCpAgVfSGESBEq+kIIkSJU9IUQIkWo6AshRIpoirNzY8xC4C7gWmvtjcaYI4AvAYNA\nH3CWtbYnTg1CCCEKxHamb4xpB24A7g28fA3wIWvtu4EHgY/FNb4QQojRxHl5ZwA4Dngh8NoWYOfs\n353ZWAghRELEdnnHWjsEDBljgi9fCNxnjOkBeoDPu/oYGhoeaWpqjEuiECLLRdfdx4ZNvfl4/uwO\nrrngyLJyT/yHu0a99uOrTyqrvVa55bRPcBpKNcR6TX8MbgBOttb+xhhzFfAJ4PpSG/f09EcarKtr\nOps3b43URxxIV2VIV2WMR1dHe8uoOMq++XJd7cG2BiBoFNNQQW4c7UkS5fjq6ppesi3pu3f2t9b+\nJvv3z4HFCY8vhBiDs47Zm4MX7Mrc3aZz8IJdOeuYvcvOPe/kfZzxsqXzSsa+3AtP2y9/ytqQjXMc\nbGaEti2Ojz90d2e8aM9pzniy0hC34ZoxZjmwJXv3zqPAadbaJ4wxXwAarLX/Wip38+atkcRNpjOx\nJJCuypCuypCuyoh4pp/85R1jzEHA1cBcYNAYcyrwceD/GmMGgVeBc+MaXwghxGji/CH3YeCoMZre\nFdeYQggh3GhFrhBCpAgVfSGESBEq+kIIkSJU9IUQIkUkvThLCJEy1j+9mevuXM8IhXvtF87tAuCN\n/h3c+rOn2Ny7ja6OqZx1zN5Mm1pYKPa97ie556GCk8vxh+7O+45cAMCnruqmb6gwzrQWuP6i9+Tj\nq25byxObCgs8F85p46Jlh+Tjm3+4jrVPFvwel+zbyYdPPNCrGeCl/+rjytWP0LdtkPbWZi4+YxG7\ndbZHmabE0Jm+ECJWcsUTMqtrr129Pt9268+e4vdPvsLGl7by+ydf4dY1T4VygwUf4Ke/LcTBgg/w\nxo5wHCz4AI89F46DBR/gwccLsUszwJWrH6Fn6wA7ht6k540BrvzuI0wUVPSFELFSvMIyGG/u3RZq\nK45rhUszQN+2QWdcz6joCyFipXhpaDDu6pgaaiuOa4VLM0B7a3M4ntrMREFFXwgRKy7/HJ/nj8s/\nZ1rYI25UvHBOmzNesm9nydilGeDiMxbROX0KLU070Tl9ChefvoiJQuzeO1GQ906ySFdlSFdlSFdl\nxOW9ozN9IYRIESr6QgiRIlT0hRAiRajoCyFEilDRF0KIFBGrDYMxZiFwF3Bt9slZzcC3gL2ArcCp\n1toeVx9CCCGqR2xn+saYdjIPQr838PJHgM3W2ncCdwCHxzW+EEKI0cR5pj8AHAd8LvDaicAXAay1\nN8c4thCpI2de1tu3g472llHmZS58BmIuYzSfOZlL15rfPcsdv3w2v+2ypfM4enHhwennrugepfUb\n//geb1vUdl+uy6zNZyJXa2I707fWDllri4005gLHGmN+ZYxZbYx5a1zjC5E2cuZlGzb1jmle5sJn\nIOYyRvOZk7l0BQs+wO2/CMf1isuszWciV2uStlZuAKy19nJjzBeAzwMXl9q4s7ONpqbGSAN2dU2P\nlB8X0lUZ0uWnt2/HqLhcff3bB0fFwVxX32OZk5WbOxY+zXHlVqvvKO9DpWOOh6SL/svAfdm/1wCX\nuzbu6el3NXuZjMur40S6KqPedHW0t4yKy9XXNqWZgcGBQtzaHMp19d1AuPA3QNm5Y+HTHFdutfqO\n8j4EiWjDULIt6aJ/D/BeYBVwEGATHl+ISUvOrCx47bxcLj5jEVd+N3tNf2rzKAOxXF/B69Q5Ljxt\nP65dHb6mX66uZUvnhS7pLFs6j4nAkn07Q5d0gmZtrrmqB2IzXDPGHARcTeY6/iDwV+B04P8As4A3\ngLOttS+X6kOGa8kiXZUhXZUhXZURl+FabGf61tqHgaPGaHp/XGMKIYRwoxW5QgiRIlT0hRAiRajo\nCyFEilDRF0KIFKGiL4QQKSLp+/SFmNTUq++Kz1vH55/zzPO9rLx9HYPDIzQ3NnDJmQey56wOwL/P\n3+t+knseeiEfH3/o7rzvyAWA28MG6td754pVv+bPLxdW3u41q4VLzz4MqN9jIIfO9IWoIvXqu+Lz\n1vH55+QKPsDg8Agrv7Mu3+bb52DBB/jpbwuxy8OmngkWfICnXyzE9XoM5FDRF6KKbO7d5oxrRd+2\nQWc8ln9OkFzBHyuu132uFfU+Hyr6QlSRro6pzrhWtLc2h+Op4bh4+WZx3NzYUDKu132uFfU+Hyr6\nQlSRs47Zm4MX7Mrc3aZz8IJd68Z35eIzFtE5fQotTTvROX3KKG+dC0/bL1/ox/LPueTMA/OFPndN\nP4dvn48/dPeScdCzZqy4XtlrVkvJuF6PgRyxee9UA3nvJIt0VYZ0VYZ0VUZc3js60xdCiBShoi+E\nEClCRV8IIVKEir4QQqQIFX0hhEgRsRZ9Y8xCY8wzxpjzi14/xhhTv7cNCSHEJCU27x1jTDtwA3Bv\n0eutwOeBF+MaW4g4yXmrBJ/5mvNW8Xnc+Lhv3Sa+tWZDPj7nuPkcvv9sANb87lnu+GX4ebJHLy48\nU9bVftcDG7jrN5vybaccMZsTlszPx8tvuZ+/bBnKx3N3beKyc4/Ix5+5pputAeeBGa1w3QXRPXBq\nlRtn35+6qpu+wlQyrQWuv6iQ6/IxSoI4z/QHgOOAF4pevxT4CrBjVIYQE4Cct8qGTb2jvFV8Hjc+\nggUfYNXdhThY0IHQA8V97cGCD/D9+8NxsOADbHwlHG8t+rS+vr1YucjRF5463iiaO5ePURLE+Yzc\nIWDIGJN/zRizN3CAtfYyY8yVvj46O9toamqMpKOra3qk/LiQrsqoJ129fTtGxTl9/dvDnjb92wcj\na3fl+/qOK7dedU2EfRoq8jEaGh4pmRvHcZ+0tfK1wKfL3binpz/SYJNxpV2cSFd5dLS3jIpz+tqm\nNDMwOJBva2ttjqzdle/rO67cetU1EfapqbEhZFjX1NgwZm7EFbkl2xK7e8cY8zZgAXCbMWYtMMsY\nc19S4wtRLXLeKvNnd4zyVvF53Pg457j5JeNlS+eF2iqJTzlidqitOJ67a5MzntGKMxYFprW4Y5eP\nURLE7r1jjFkObLHW3lj0+kZr7VxXrrx3kkW6KkO6KkO6KiMu75047945CLgamAsMGmNOBU6x1r4a\n15hCCCHcxPlD7sPAUY72uXGNLYQQYmy0IlcIIVKEir4QQqQIFX0hhEgRKvpCCJEikl6cJeoQl5dM\nGsnNx+bebXR1TB01H+uf3sx1d65nhMLzZBfO7QLgocdf5KYf/ym/7Xkn78PBZlZZueD2ZfHlunx7\nfLpWfPtBnnqh4K2wYI9WLjlzST6+6ra1PLGpsFhy4Zw2Llp2CJBO7x2Xv47v+PG1x43O9IXTSyaN\n5OZj40tbx5yPXOEFGAGuXb0+3xYsrABf+0E4duWC25fFl+vy7fHpChZ8gCefD8fBgg/w2HPRVstP\ndFz+Or7jx9ceNyr6gs2925xx2vDNR/GKwUpWEPpyB4t8WYJxlHFFcviOn1p/3lT0BV0dU51x2vDN\nR/FSx5JLH8fAl5tbnj9WHGVckRy+46fWnzcVfeH0kkkjufmYu9v0MefjwtP2yxfc3LX1HOedvE9o\n2+LYlQtuXxZfrsu3x6drwR6tznjhnDZnnDZc/jq+48fXHjexe+9EQd47ySJdlSFdlSFdlRGX947O\n9IUQIkWo6AshRIpQ0RdCiBShoi+EEClCRV8IIVJErDYMxpiFwF3AtdbaG40xs4FVQDMwCJxprX0p\nTg1CCCEKxPnkrHbgBuDewMtXADdba//dGPNJ4CLgkrg0iPh56b/6uHL1I/RtG6S9tZmLz1jEbp3t\nZeWW61EyHk8gX99RdOdy+7cP0jYlnLvmd89yxy+fzW+7bOk8jl5ceFatzwPn5h+uY+2TPfl4yb6d\nfPjEA71tAB9Z0c1wQGcTcHMd+NTUY26cfX9oRXdotfROwC2BXJdHUhLEeXlnADgOeCHw2ieA/8j+\nvRnYOcbxRQJcufoRerYOsGPoTXreGODK7z5Sdm65HiXj8QTy9R1Fdy53YHB0brDgA9z+i3Ds88AJ\nFnWABx/vKasNCBV8gCJ7GJEQxYuL3iyKXR5JSRDn4xKHgCFjTPC1PgBjTCPwSeBfXH10drbR1NQY\nSUdX1/RI+XExWXT1bx8cFZfbR2/fjlFxMNfXHqXvKLorzfX1G6W9Vrn1qmuy7VMcdSJxa+Vswb8V\n6LbW3uvatqcnmpPfZFxpFyfj0dU2pZmBwYFC3Npcdh8d7S2j4mCurz1K31F0V5rr6zdKe61y61XX\nZNqniCtyS7bV4u6dVcAGa+3lNRhbVJmLz1hE5/QptDTtROf0KVx8+qKyc8v1KBmPJ5Cv7yi6c7lT\nmkfnLls6L7RtcezzwFmyb2fJ2NUGo8/g9LCM2lBcVItjl0dSEsTuvWOMWQ5syd69cwbwbmvth8vJ\nlfdOskhXZUhXZUhXZcTlvRPn3TsHAVcDc4FBY8ypwK7AdmPMr7KbPWGt/URcGoQQQoSJ84fch4Gj\n4upfCCFE5WhFrhBCpAgVfSGESBEq+kIIkSJU9IUQIkXoVt5Jgs9rZiLi8rjx4fO4cc2Xz5fH5Qnk\nG3f905u57s71jFB4zu3CuV359lU/eZQHHtuSj488YBfOPnZ/AO56YAN3/WZTvu2UI2ZzwpLCPd4u\nbx5XvwCfu7GbzW8U5m/mDPjyJwp+MVes+jV/frmwynmvWS1cevZhgLx3itt975PvGIgbnelPEnxe\nMxMRl8eND5/HjWu+fL48Lk8g37i5DztkPFquXb0+1B4szAD3/bEQBwsJwPfvD8cubx5Xv0Co4AO8\n/Ho4DhZ8gKdfDMeigO998h0DcaOiP0nY3LvNGU9E+rYNOuMouObLN26UuS5ebRjv0khRj9T6GFDR\nnyR0dUx1xhOR9tbmcDy1ucSWleOaL9+4Uea6eJlkyWWTYtJS62NARX+S4POamYi4PG58+DxuXPPl\n8+VxeQL5xr3wtP3yH/Lc9dwgRx6wS8n4lCPCnuvFscubx9UvZK7hu+K9ZrU4Y1HA9z75joG4id17\nJwry3kkW6aoM6aoM6aqMuLx3dKYvhBApQkVfCCFShIq+EEKkCBV9IYRIESr6QgiRImK1YTDGLATu\nAq7NPjlrNpnn4zYCLwJnWWsHXH0IIYSoHmUVfWPMscDO1trvGGNuA94JfM5a+31HTjtwAxB8+Pm/\nAF+x1n7PGPMl4Fzga+NWP8mIyz/nmed7WXn7OgaHR2hubOCSMw9kz1kdiehy5fr69fnYuPbL55+z\n5nfPcscvn83Hy5bO4+jFmefZ+rxTrlv9EI9uLPgWLNpzGp9+/zsBuOq2tTyxqT/ftnBOGxctOyQf\nu/xxAC79ajcvBSwQdu+AKz6e8XT55Mputr1ZaGtrghs/W/CD+ez13bxaGJpdpsHK8+vbp2Yyeu98\naEV3aJXtTsAtgdz71m3iW2s25ONzjpvP4fuH7+WPk3Iv71wG/L9s8W8EDgQ+7ckZAI4DXgi8dhTw\no+zfPwaWlq00BcTln5MrjACDwyOs/M66xHS5cn39+nxsXPvl888JFnyA239RiH3eKcGCD/DIM4U4\nWPABHnsuHLv8cYBQwQd4obfwd7DgA/QPheNXw0OxpchPRyRD8eKiorctVPABVt29gSQp9/JOv7V2\nizHmeOBWa+0bxphhV4K1dggYMsYEX24PXM55BZg1KjFAZ2cbTU2NZUocm66u6ZHy42IsXb19O0bF\n1dA/NDwyKi7Vb7V1uXLH02+w3bVf/dvDfjn92wcr6ruStjhzpSu53HrUFUf9KrfotxpjLgbeC3zW\nGDMfeEvEsb2WEz09/b5NnEy0lXYd7S2j4mrob2psyJ8R5+Kx+o1Dlyt3PP0G21371TalmYHBws9F\nba3NFfVdSVucudKVXG696Yq4IrdkW7mXdz4KvA04x1q7HTgG+MdxaHnDGJNzp3ob4Us/qScu/5xL\nzjyQ5sbM/7G5a99J6XLl+vr1+di49svnn7Ns6bySsc87ZdGe00rGC+e0hdqKY5c/DmSu4ZeK24pO\n0YrjXaa5Y5EMxUW1OD7nuPnOOG6c3jvGmLe7kq21f/YNYIxZDmzJ3r1zM3B/9gfh64FHrbW3lMqV\n906ySFdlSFdlSFdlxOW947u8c6+jbQQo+Z+CMeYg4GpgLjBojDkVOAP4pjHmY8BzwLc84wshhKgi\nzqJvrZ3navfkPkzmbp1ijh5vn0IIIaLhLPrGmG+72q21H6iuHCGEEHES9fKOEEKICYTv8s6Y19yN\nMS3AbYDzm4AQQoj6olwbhrOAa4C3Zl96E/e3ACGEEHVIuYuzPg3sB6wGjidzF85rcYlKK1F8asbb\nb9R8n8eNq92X6yOK944rd/3Tm7nuzvWMUHiG6cK5XflclzePz7fH57viGvu2NY9z77qX89sevXgm\ny5bum4+/cucfePjpgo/DwWYG5528GIArVv2aP79cWAG916wWLj37sHzs8hMC+Oev/4q/9hQMBWbv\nvBOXf+QoAD62opvg+ucW4KaA14zLi2aieu+49nnVTx7lgce25NuOPGAXzj52/3wc9biPSrmLs16z\n1r4ENFpr+6y1N5MxSxNVJIpPzXj7jZrv87hxtftyfUTx3nHl5oouZH64unb1+lCuy5vH59vj811x\njR0s+AA//0M4DhZ8gN/bQhws+ABPvxiOXX5CQKjgA2z6r0IcNryAHUWxz4tmIuLa52DBB7jvj+E4\n6nEflXLP9IeNMScAm7KLrR4H5sSmKqVs7t1WMna1Rek3an7ftvDhX0ns29bHYJH3TjD29e3KLS5S\nSd6xUMuxRTJEPe6jUu6Z/lnA88AFwO7AmcD5cYlKK10dU0vGrrYo/UbNb29tDrW1Ty2KHe2+XB85\nC4axYl/frtzipYxek6gqUsuxRTJEPe6jUm7RP91a+4i19hVr7UettScBh8cpLI1E8akZb79R830e\nN652X66PKN47rtwLT9svX2xz19WDuLx5fL49Pt8V19hHL54Z2rY4PtjMKBnvNSv8G05x7PITgsw1\n/FJx8a9DxbHPi2Yi4trnIw/YJdRWHEc97qPi8955N/AeMmf2twaamsmYr+0Wpzh57ySLdFWGdFWG\ndFVGrbx3nqTgeR/0zx8EThuXGiGEEDXDtzjrReC7xpgHrbUbAYwxU4BdrbWbXLlCCCHqj3Lv3llm\njHkDuAV4GNhqjPmZtfaf45MmhBCi2pT7m8qJwI3A/wJ+bK3978C7YlMlhBAiFsot+oPW2hHgWOCH\n2deiPbxWCCFE4pR7eafXGPNTYA9r7W+zC7UqXlhnjJlGxqStE5gCXG6tXVNpP0IIIcZHuUX/dDIP\nP/lNNh4Azh7HeB8ErLX288aY3YFuYME4+kkdLq8YiOaPk+t7aHiEpjH6juKf89DjL3LTj/+Uj887\neR8ONpkbwtb87lnu+OWz+bZlS+dx9OLCc3t8PjWufJ9/jsun5qrb1vLEpv5828I5bVy07JB87PLX\ncfVbTvvyW+7nL1uG8vHcXZu47NwjAPjUVd30FZqY1gLXX1Sex815K7oZCLS17gRfvSQZn5p6zI2z\n789c083WgC/DjFa47oJCrs+bJ/dZ7u3bQUd7S8VeWT7KvbwzTGZF+AnGmHOB2cDScYy3Bdg5+3dn\nNhZl4PKKgWj+OLm+R0r0HcU/J1jwAb72g0IcLNgAt/8iHPt8alz5Pv8cl09NsOADPPZcOHb567j6\nLac9WPABNr5SiPvCTbxRZHLj8rgZKGrbPhkMcOqUrUXvy+vbw7HPmyf3Wd6wqXdcXlk+yj3TX0Om\n8D8XeG0E+EYlg1lrVxtjPmiMeZpM0T/etX1nZxtNTdF+Oujqmh4pPy4q1TVU5BUzNDwS6qO3L3yk\n9fbtyLf3bw97e/RvHwzl+vp25fv6HgtXe5TcYPtYHja10lWtfaqn3HrVNRn2yfVZrgblFv1ma+2R\nUQczxpwJ/MVa+15jzAHAvwGLS23f09NfqqksJtNKu6bGhpApWFNjQ6iPjvbw17+O9pZ8e9uUZgYG\nC+d6ba3NoVxf3658X99j4WqPkhtsbyBc+Bsi9l0P+1RPufWqazLsk+uzXC6u/yTKvbzzuDFmZ/9m\nXt5F5lsD1to/ArsbY3QXUBm4vGIgmj9Oru+GEn1H8c857+R9SsbLls4LtRXHPp8aV77PP8flU7Nw\nTluorTh2+eu4+i0nnrtrU8l4WtFl3eLY5XHTWtRYHIvqMaPVHfu8eXKf5fmzO8blleXD6b2Twxhz\nD3AI8Ccgf2XRWntEJYMZY/4BmGmtvcQYMwf4ubW25B7JeydZpKsypKsypKsyauW9k2PFuEYezdeB\nbxhj7suO/fEq9SuEEKIMnEXfGJP7EvhANQaz1r5BZlWvEEKIGuA70x9i7If35H4n0/V4IYSYQPhc\nNvVzjxBCTCJU1IUQIkWo6AshRIoo9+4dUSYuD5xajVuub08prw+Xv45vf+P0BHLtl2+fXd48Pk+g\nKJ4/Pj+hm3+4jrVP9uTjJft28uETM+smvtf9JPc89EK+7fhDd+d9Rxasq1yeLiu+/SBPvVDwA1iw\nRyuXnLkkH1/61W5eCjhC7N4BV3y84Bfjyv/cjd1sfqOQO3MGfPkThVyX74/PE+hjK7oJrvluAW5K\nwHvns9d382pgbegu02Dl+YVclw+SL9fl3QT+4z4qOtOvMi4PnFqNW65vTymvD5e/jm9/4/QEcu2X\nb59d3jw+T6Aonj8+P6FgwQd48PFCHCz4AD/9bTh2eboECzbAk8+H45fCFkC80BuOXfnBgg/wclFf\nLt8fnyfQYFF7ka1NbLxaZAawpWgfXT5IvlyXdxP4j/uoqOhXmc2925xxLcYdLPLWKY59mvu2DZaM\nfbmu2NVvObpdsW/bsbx5qkFc/Yr04Dt2o6KiX2W6OqY641qMm7NvKBX7NLe3Nofjqc0lt60kdvVb\njm5X7Nu2eLliyeWLFRJXvyI9+I7dqKjoVxmXB06txi3Xt6eU14fLX8e3v3F6Arn2y7fPLm8enydQ\nFM8fn5/Qkn07S8bHH7p7qK04dnm6LNgjbABTHO9edMm4OHblzwzbB42KXb4/Pk+g4l/D4v91LMMu\n09yxywfJl+vybgL/cR+Vsrx3aoW8d5JFuipDuipDuiojLu8dnekLIUSKUNEXQogUoaIvhBApQkVf\nCCFShIq+EEKkiMRtGIwxZwCXkLFtvsxa+9OkNQghRFpJtOhnn7P7ReAgYBpwOVD1oh/FuyKqd045\nPjVxeNy4PF98fjAPPf4iN/34T/n4vJP34WAzqyxdvlyXz4jPH8f3PkbxwHHp8u3Tdasf4tGNhbX1\ni/acxqff/05vv+D3z7ltzePcu+7lfHz04pksW7ovAFes+jV/frmw3n+vWS1cevZh+fgz13SzNWAH\nMKMVrrsg4/ly1W1reWJTwR9g4Zw2Llp2SD729f2RFd0MF7qmCbg561Nz4XXdvBZwaehsg6s//Z6y\ncqP448TpvRNnrstPqJz8qCR9eWcp8Atr7VZr7YvW2o/GMUgU74qo3jnl+NTE4XHj8nzx+cEECxzA\n134Qjl26fLkunxGfP47vfYzigePS5dunYMEHeOSZQuzzVfH55wQLPsDP/1CIg0UZ4OkXw/HWImOa\n1wOFOFjwAR57Lhz7+h4mTNB65rWwLQ89Rd4zrtw0Uis/oRxJX96ZC7QZY34EdALLrbX3ltq4s7ON\npqbKH841VORVMTQ8QlfX9LJye/t2jIrLzQXo3z44Ks7l+/qOkjuW50uu3dVWinJ1+XJd7b73aTzv\nY7X2uZK2OHOlK7nciaqrUpIu+g3AzsDJwBzgl8aYOdbaMVfe9hSfMpRJU2NDyKSoqbGh7JVtHe0t\no+JKVsW1TWlmYLDgHdjW2pzP9/UdJTf3/MpgnGt3tZWiXF2+XFe7730az/tYrX2upC3OXOlKLnei\n6hoL138SSV/eeRl40Fo7ZK19BtgKdHlyKiaKd0VU75xyfGri8Lhxeb74/GDOO3kfZ+zS5ct1+Yz4\n/HF872MUDxyXLt8+LdpzWsnY56vi8885evHMkvFes8L/8RfHM8L2OKF44Zy2UFtx7Ou7+OwwGHeG\nuxoVu3LTSK38hHIk6r1jjHkb8E3gGDKXd/4TmGetfXOs7eW9kyzSVRnSVRnSVRmTwnvHWvtX4E5g\nLXAP8KlSBV8IIUT1SfyblrX268DXkx5XCCGEVuQKIUSqUNEXQogUoaIvhBApQkVfCCFSxKS8ZTaK\n90694vPeieoZFJcul2+Pqy3q2HHqcnn+RH0fXH5EPk8gl7eTL/e+dZv41poN+fic4+Zz+P6zy2r3\n+Ryt+smjPPDYlnx85AG7cPax+5eVe/MP17H2yZ58vGTfTj58Yma9hs/H6HM3drM54JgxcwZ8+RMF\nD5uv3PkHHn769Xx8sJnBeScvBmDFtx/kqRcK/hIL9mjlkjOXlJXr8mYC9/EDcN6KbgpLITPPDf7q\nJRPXeycRonjv1Cs+752onkFx6XL59rjaoo4dpy6X50/U98HlR+TzBHJ5O/lygwUdYNXdG8pu9/kc\nBQs+wH1/LMS+3GDBB3jw8ULs8zHaHLZI4uXXw3GwaAP83hbiYMEHePL5cOzKdXkzgfv4AUIFH2B7\nlW9qn5RFf7DIs6U4nohs7t0WKY4L37h92wZLxq62qGPXSlfU9yHKsVurY2Asn6MkcsX4mJRFP7e0\nv1Q8EenqmBopjgvfuO2tzeF4anNZbVHHrpWuqO9DlGO3VsdAscJKPm1RcsX4mJRFP4r3Tr3i896J\n6hkUly6Xb4+rLerYcepyef57/qiuAAAN7UlEQVREfR9cfkQ+TyCXt5Mv95zj5o879vkcHXnALiVj\nX+6SfTtLxj4fo5kzcMYHmxkl4wV7hI2MimNXrsubCdzHD2Su4bviqCTqvVMp8t5JFumqDOmqDOmq\njEnhvSOEEKK2qOgLIUSKUNEXQogUoaIvhBApQkVfCCFSRE2KvjFmqjHmGWPMB2sxvhBCpJVaee98\nAXg1rs59PiO1wuWN4iOqT01cuqJ4ApWbW0qXK9/lYRNVl8t3xYfPa8al25frOu59x0+Uvn1zvfyW\n+/nLlqF8PHfXJi479wjA7/lz25rHuXfdy/n46MUzWbZ0X8D/Prg8f3z5V6z6NX9+eUe+ba9ZLVx6\n9mH52OXN49rfcnSdu6KbYr7xjxPYe8cYswB4B/DTuMbw+YzUCpc3io+oPjVx6YriCVRubildrnyX\nh01UXS7fFR8+rxmXbl+u67j3HT9R+vbNdbAAAmx8pRD7PH+CBR/g538oxL73weX548sPFnyAp18M\nxy5vHtf+lqMrbmpxpn81cD5wtm/Dzs42mpoaqzJoV9f0qvQThd6+HaPicnX1bx8cFVdrn6Lo8uW6\n2qPk+tqHijxrhoZHqqZrLMqdr7G8ZoK5Lt2+XJcu3/ETpW/fXLtyK22LM3ei6qqURIu+MeYDwG+t\ntc8aY7zb9/T0V23selhx19HeMiouV1fblGYGBgv+e22tzVXbpyi6fLmu9ii5vvamxoaQWVlTY0PV\ndI1FufPVQLjANhTlunT7cl26fMdPlL59c+3KrbQtztyJqmssXP9JJH1553jgJGPMWuDDwD8bY5ZW\nexCfz0itcHmj+IjqUxOXriieQOXmltLlynd52ETV5fJd8eHzmnHp9uW6jnvf8ROlb99cz921qWTs\n8/g5evHMkrHvfXB5/vjy95oV/o+/OHZ587j2txxdcVMz7x1jzHJgo7X2m6W2kfdOskhXZUhXZUhX\nZch7RwghRGRq9rhEa+3yWo0thBBpRWf6QgiRIlT0hRAiRajoCyFEilDRF0KIFKGiL4QQKaJmd+/E\nSc4Aamh4hKYxDKBEmCiGaxMVn6laOblJz1cUg7ooxnjV0j2e+fKZubnwmcy56kQUg8MommESGq4l\nQW7CRxjbAEqEiWK4NlHxmaqVk5v0fEUxqItijFct3eOZL5+ZmwufyZyrTkQxOIyiOQkmZdEfLDKA\nKo5FmM2925zxZCTKPtdqvnzjuuIouVGJ0neUz3LftkFn7Orbl+ui3uvPpCz6OR+QUrEI09Ux1RlP\nRqLsc63myzeuK46SG5UofUf5LLe3NofjqeHY1bcv10W915/G5cuX11pDSfr7dywfT9473t7J2sde\nYmSkYAD11umt/sSEaG+fQn//Dv+GCbHPnA62vLad9qnN7Ln7DM46Zm9amqtjaV0N4piv3D63NO3E\n/D06KtrnWs2XT7NLV7m545mPcnWPZ75yn+U3x/FZPmD+zvznU1t4880RZrS3cPHpi0K/JbjqhC83\nLs0Ad/362VGvnXTYvLLzAdrbp1xeqq1mhmvlIMO1ZJGuypCuypCuypDhmhBCiMio6AshRIpQ0RdC\niBShoi+EECki8RW5xpiVwOHZsb9srf1+0hqEECKtJHqmb4x5N7DQWnso8F7guiTHF0KItJP0mf79\nwEPZv3uBdmNMo7V2uJqD5Hwz+rcP0jalMt8MIXzUq7dTFI+bOL137lu3iW+t2ZCPzzluPofvPzuy\nrqia45qv9U9v5ro71zNC4SHzC+d2la1rUnnvWGuHrbV92fBDwN3VLvhQ8M0YGKzcN0MIH/Xq7RTF\n4yZO751gwQdYdfeGEltWpiuq5rjmK1fwAUaAa1evr0hX3NTEZdMYcxKZov+3ru06O9toaqp8VWD/\n9sFRcVfX9Ir7iZN605NDuvwMFXmpDA2P1IW+3r4do+JydUXJHQ/V0BVVc1zzVbyidITox28134ta\n/JB7DPBPwHutta+5tu3p6R/XGG1TmhkYHCjErc11teJuMq4AjJN609XU2BAy0WpqbKgLfR3tLaPi\ncnVFyR0P1dAVVXNc89VAuPA3UP7+lqLSfNd/Eol67xhj3gLcTqbgb/FtP17vnZxvxshI5b4ZSVBv\n3js5pKs86tXbKYrHTZzeO2+d0cQjG17Nx+ccN585M98SWVdUzXHN1557TGPtY68AhWv6u3aU/5vi\npPLeMcZ8FFgOBC+efcBa+5extpf3TrJIV2VIV2VIV2XE5b2T6OUda+3NwM1JjimEEKKAVuQKIUSK\nUNEXQogUoaIvhBApQkVfCCFShIq+EEKkiJqsyE0rUbw+hBDp4K4HNnDXbzbl41OOmM0JS+ZXrX+d\n6SdIFK8PIUQ6CBZ8gO/fv6nEluNDRT9BNvduc8ZCCBE3KvoJ0tUx1RkLIUTc6Jp+gpx1zN4AoWv6\nQggR5JQjZocu6ZxyRHnPHigXFf0EmTa1hfP+58K69foQQtSeE5bM54Ql82OrE7q8I4QQKUJFXwgh\nUoSKvhBCpAgVfSGESBEq+kIIkSJq8Yzca4FDyDxG8jPW2t8nrUEIIdJKokXfGHMkMN9ae6gxZh/g\nG8ChSWoQQoh65pnne1l5+zqGhkdoyj6Dec9ZHVXrP+nLO/8D+CGAtfZPQKcxZkbCGoQQom5Zefs6\nBodHGAEGh0dY+Z11Ve0/6cs7uwEPB+LN2ddeH2tj18N9y6Wra3rULmJBuipDuipDuiqjnnQNDo8M\nEzghHxweebOra3pjtfqv9YrcyEVdCCEmEz+++qSqFfixSPryzgtkzuxz7A68mLAGIYRILUkX/Z8B\npwIYY/4b8IK1ViY0QgiREA0jIyOJDmiMWQEcAbwJfNJa+8dEBQghRIpJvOgLIYSoHVqRK4QQKUJF\nXwghUkStb9msGsaYhcBdwLXW2huL2pYCXwKGgbuttf9aJ7o2ApuyugDOsNb+NSFdK4HDyRwDX7bW\nfj/QVpP58mjaSA3myhjTBnwTmAm0Av9qrf1JoL1Wc+XTtZEaHVvZ8acCj2V1fTPwes0+ix5dG6nN\n8XUU8D3g8exL6621nwq0V32+JkXRN8a0AzcA95bY5HrgGOCvwH3GmP+w1j5RB7oAjrXWvhG3liDG\nmHcDC7N2GDsD64DvBzZJfL7K0AQ1mCvgROAP1tqVxpg5wM+BnwTaa3JslaELajNfOb4AvDrG67Wa\nL58uqN183WetPbVEW9Xna7Jc3hkAjiOzDiCEMebtwKvW2k3W2jeBu8nYQdRUV425H3h/9u9eoN0Y\n0wg1na+SmmqJtfYOa+3KbDgbeD7XVstjy6Wr1hhjFgDvAH5a9HotP4slddUrcc3XpDjTt9YOAUPG\nmLGadyNj95DjFWDPOtCV4yZjzFzg18DnrbWx305lrR0G+rLhh8h8bcx9ra3JfHk05Uh8rnIYYx4E\n9gBOCLxcs2PLoytHrebrauB84Oyi12s9X6V05ajVfL3DGPMj4K3A5dban2dfj2W+JsuZfiXUk/XD\nZcBFwFHAQuB9SQ5ujDmJTIE937FZovPl0FTTubLWLgH+DviOMabUnCR+bDl01WS+jDEfAH5rrX22\njM0Tm68ydNXq+NoAXA6cROY/o38zxrSU2LYq8zUpzvQ9FFs/vI06udxirf127m9jzN3AfsCdSYxt\njDkG+Cfgvdba1wJNNZsvh6aazZUx5iDglexX7EeMMU1AF5mzrlrOlUtXLY+t44G3G2NOIPMNZMAY\n87y19hfU9rPo0lWz+cr+WHxHNnzGGPMSmXl5lpjma9IXfWvtRmPMjOzXtufJfA0+o7aqwBjzFuDf\ngROttTuAI0mu4L8FuBJYaq0N/ahVq/lyaarlXJFZPT4HuMAYMxOYBmyBmh9bJXXVcr6stX+f+9sY\nsxzYGCisNZsvl64afxbPAGZZa68yxuxG5m6sv2Y1xzJfk6LoZ896rgbmAoPGmFOBHwHPWmt/AJwH\n3J7d/A5r7VP1oCt7RrHWGLONzN0qSRWyvwd2Af498HtDN5nbxWo1X05NNZyrm8h85X4AmAp8EviA\nMea1Wh5bPl01nK9RGGM+CNR6vpy6ajhfPwK+m72s2UJmfk6P8/iSDYMQQqSINP6QK4QQqUVFXwgh\nUoSKvhBCpAgVfSGESBEq+kIIkSImxS2bQoyX7D3QFvht4OUm4FJr7f2OvDOttd/J3lt9g7X2/aW2\nFaKe0C2bItXkvFastXsEXnsH8AvgbWP5r2SN4P5krd07MaFCVAmd6QtRhLX2iazv+t8YY64hY4Q1\nHfietfZ/A98A5hhjfgZ8lOx/GsaYb5JZJr8fsDfwb1nr453JLLBpJ+O18jfAl3IrQoVIEl3TF6II\nY8zfkXE33An4obX23cC7gEuNMTOALwKbrbV/O0b62621JwJ/S8ZHCOBC4DFr7buAq4DD4t4HIUqh\nM30hoMsY86vs338DPEfG5+QV4HBjzHnADjJPqHqrp69fAVhrn8v6pjQCi4Cbs68/ZoyxVd8DIcpE\nZ/pCZM7aj7LWHgVcTOZzsQG4AJgCvCvbtrWMvoaK4oZsf28GXit+ToAQiaGiL0QAa+1/AD1k/Pxn\nAk9Ya0eyl3zayPwn8CbQXEG3TwJLIP8j8YKqihaiAlT0hRjNJ4HPk3nw+AeNMd3APOC27L8XgJeM\nMQ+T+XHWxzXAe7KOmJ8BHmb0NwIhEkG3bAoRMybjFf12a+092buCngHeaa2tm+faivSgoi9EzGQX\ncN1K5kEnTcCt1trra6tKpBUVfSGESBG6pi+EEClCRV8IIVKEir4QQqQIFX0hhEgRKvpCCJEi/j9S\n2H22uWEMZAAAAABJRU5ErkJggg==\n",
            "text/plain": [
              "<matplotlib.figure.Figure at 0x7feccf580860>"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\nRU5ErkJggg==\n",
            "text/plain": [
              "<matplotlib.figure.Figure at 0x7fecd20b5ac8>"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<matplotlib.figure.Figure at 0x7fecd220de48>"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<matplotlib.figure.Figure at 0x7fecd214ba20>"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<matplotlib.figure.Figure at 0x7feccf55fa90>"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAX0AAAEKCAYAAAD+XoUoAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4yLCBo\ndHRwOi8vbWF0cGxvdGxpYi5vcmcvNQv5yAAAIABJREFUeJztnXt4VfWV9z8hF0ISaFIMCMojDsLC\nqhVfwanWC3ZgaNXWB2s7ojBW7Y3W2toqbZ2pgzO+U14syqi96OvUtmilb5221toOXlIvrbWogxWt\n/ESrFi9A0EQhQEhC3j/OOck+t511TvY+5+zs9XkeH7NO1vn9vnvt317Z7HP2d1f19/djGIZhxINR\n5RZgGIZhlA5r+oZhGDHCmr5hGEaMsKZvGIYRI6zpG4ZhxAhr+oZhGDGiJszBReRI4C7gOufcjSJy\nMvDvQA/QBSxxznWEqcEwDMMYJLQzfRFpBG4AHvC8fC1wkXPuVOBR4DNhzW8YhmFkE+blnW7gNOB1\nz2s7gPHJn1uSsWEYhlEiQru845zrBXpFxPvypcBDItIBdABf9xujt7evv6amOiyJgfHl1Q+xeUvn\nQDx9SjPXfumUUOf88Ffuynrt7lVnhjZfkNsYh3pVKuWog2bOIHUFOdbZX7ub7p79A/Ho2lHcueLD\nRc35ka/chdf/oAr4ZXi1r8r3i1Cv6efgBmChc+73IvIt4HPA9fmSOzp2D2uy1taxtLfvHNYYGpob\n67Li4c5bjPYwt7XQbfTTH0a9iiHfnKVaN2Hhp78KshpP2NuqmTNsXcWO1TC6lu6e7sG4vlY9VmZe\nTXUVPX39aXFYtW9tHZv3d6X+9s57nXO/T/58HzC7xPOHwpIFM5gzcwJTDxzLnJkTWLJgRuhzThk/\nyjcOmiC3sRz1uuC06b5xXLj0nKMGTgGrknElzBmkrrNOnuIbF8Ll582iZexo6mpG0TJ2NJefOytn\n3tKFh/vGAMsWH0NtdWIra6urWLb4mKJ1DYeqsA3XRGQ5sCP57Z2ngXOcc38WkX8Gqpxz/5bvve3t\nO4clLspnbFHWDtHWH2XtEG39UdYOlaO/tXVs6S/viMixwCpgKtAjImcDnwX+r4j0AG8BF4Y1v2EY\nhpFNmB/kPgnMzfGr94c1p2EYhuGP3ZFrGIYRI6zpG4ZhxAhr+oZhGDHCmr5hGEaMKPXNWUZAXH3r\n7/jLtn0D8WGT6rji/BPLqEjPi692svKODfT09Q98X3napOZQ59TUa9fufay593k6u/bR3FjHkgUz\naBpTlzlUpHlowxZ+uG7zQHzBadM56b3Ff489KG5f9ywPbNg2EM+fPZFF844oaqwgt/GnbZv4zfpB\nJ5nTj5/MR0+ZWdRY5Vj3ubAz/YjibWAAL7yxL09m5ZFa+AA9ff2svG1D6HNq6rXm3ud5fNN2Nm/p\n5PFN21mz7vnQdZUabzMEuPXXm/NklhZvwwe474lteTKHJsht9DZ8gHv+8HqezKEpx7rPhTV9o+R4\nb0XPFZeL9s49vrFhDIdKWffW9I2Sk7oVPV9cLlqbx/jGhjEcKmXdW9OPKIdNqvONK5lyeJBo6pXy\nBJo+pblknkClplI9iObPnugbF0KQ23j68ZN940KIjffOcDDvnWhqh2jrj7J2iLb+KGuHytHv571j\nZ/qGYRgxwpq+YRhGjLCmbxiGESOs6RuGYcQIa/qGYRgxIlQbBhE5ErgLuC755Kxa4IfAYcBO4Gzn\nXEeYGgzDMIxBQjvTF5FGEg9Cf8Dz8qeAdufcccBPgJPCmt8wDMPIJswz/W7gNOCrntc+DPwLgHPu\n5hDnLilag6cgDZcuXNGW9dr3v/aBosba+EI7q+/cSD+DD6U+cmprWk6QhlifWtFGnyeuAW7OoV2j\nS4umXuUwXEvN2d65h9bmMTnnDLIOQbJ67XqefnnXQDxrWhOXfOy4rDxN7bXr+Rs3PchrHfsH4inj\nR3HVp+am5WjNCDV1/fzKNvYMTkdDDdx4WbYuzfFx1yObuev3Wwbis06ewhknlP7muNDO9J1zvc65\nTPOSqcCHRORBEVkrIu8Oa/5SojV4qhTDpUxSCx+gH7hu7casnCANsfoy4t5h6AqSchiupeZ8eevO\nvHOWug5avA0f4KkXd+XJDA5vwwfY8ub+rBytGaGmrnsyht+dZ7Fqjg9vwwf42cNbsnJKQamtlasA\n55y7SkT+Gfg6cHm+5JaWBmpqqoc1YWvr2GG9P8h5ezMMlnr7+n31Faq92G3NvO25XznWUDmF6MmV\nW6yuYufs7NqXFYe9fjRzFlOHSlr3xeaFPVZY6364usKm1E1/G/BQ8ud1wFV+yR0du4c1WTlvic41\nb011VZqzXk11VV59xWgvdlurSD8AqpRj+eUUqj9XbrG6ip2zubEuKw57/WjmLLQOlbbui80Le6ww\n1n0QuoLA749Jqb+y+Rvgg8mfjwVciecPBa3BU6UYLmVy6TlHkTLqSF3bzCRIQ6zMM418Zx4aXUFS\nDsO11JxTDxybd85S10HLrGlNvnEYTBk/yjcGvRmhpq4NNf5xCs3xcdbJU3zjUhGa4ZqIHAusInEd\nvwd4DTgX+A9gErALON85l/fisBmuRVM7RFt/lLVDtPVHWTtUjn4/w7XQLu84554E5ub41cfCmtMw\nDMPwx+7INQzDiBHW9A3DMGKENX3DMIwYYU3fMAwjRljTNwzDiBGlvjmrJJTDQ0XDuj++xE9++9JA\nvGjeocyffWhRYwXphaNh/bNv8L27nxuIly48nDkyqaixtD4rW9/s4pq1T9G1p4fG+louP28WB7Y0\nhjZnkNuoReO9E2QdNPNp0XrJLF3RRrcnrh8F31mWXnutj8+tv3qaR57ZMRCfcvQBnP+h9xY1luYY\nunR1G2/vHYxbGmDVJdlrVeO/pdEO4a/DEXmmXw4PFQ3ehg9wx/0v5ckcmiC9cDR4FyHAd3/+XJ7M\n4Lhm7VN07OxmX+9+OnZ1c82Pnwp1vnJso8Z7J8g6aObTovWS6c6I92bb5ah9fLxNE+ChP+3IytGO\npTmGvA0fIJ9JgMZ/S6Mdwl+HI7Lpt3fu8Y2NaNC1p8c3Hglo1mqQdbBjwxiRTb+1eYxvbESDxvra\n9HhMbZ7M6KJZq0HWwY4NY0Q2/XJ4qGhYNO9Q37gQgvTC0bB04eG+cRhcft4sWsaOpq5mFC1jR3P5\nubNCna8c26jx3gmyDpr5tGi9ZOpH+ceg9/E55egDfONCxtIcQy0N/nEKjf+WRjuEvw5D894JAvPe\niaZ2iLb+KGuHaOuPsnaoHP1+3jsj8kzfMAzDyI01fcMwjBhhTd8wDCNGWNM3DMOIEdb0DcMwYkSo\nTV9EjhSRF0Xk4ozXF4hI5X5tyDAMY4QSmveOiDQCNwAPZLxeD3wdeCOsuTXeFVo/E41XyRevbWPn\nvsF4XD2s/lK2P8fyWx7mrzt6B+KpE2q48sKTc+ravbeHhtH5dWm8ZK6+9Xf8ZdugsMMm1XHF+Sdm\nve+iFW1pD4geBdySMZbWL0eDdixNvbTbqJlTq0vjobLxhXZW37mRfgafv3rk1NassTRrR+vZokGz\nr0G37rX1CrL2UR5LW/sg93cuwjzT7wZOA17PeP0K4NvAvqx3BITGu0LrZ6LxKtmZsSXv7M1KAUhr\nYAAvb+/Nyknp6u4Zvs+KtxkCvPBG7pJn/pMrhzVKWdDUS7uNQaLxUEk1fEjU97q1G3OOpVk7Ws8W\nDdp9HaRHj5FAW/sg93cuwnxGbi/QKyIDr4nIDOBo59yVInLNUGO0tDRQU1MdiJ7W1rFp8e69PVlx\nZg5AZ9e+rDhX3lDzBa2r2DlLOZZ2rkJyK20b8+VlHuD9JdY13NqXet3bWMHkaSi1tfJ1wCXa5I58\nlnZFkHmXXMPoWrp7Bv3/Guprc95J19xYlxVr7rjT3pVXrK5i5yzVWIXemRjFbfTLqyK98VeVUFcQ\ntS/1urexgslL4fdHomTf3hGRg4CZwO0i8hgwSUQeCmMujXeF1s9E41Uyrt4/TjF1Qo1v7NU1unb4\nPiuHTarzjVNkLoJK+UqXpl7abQwSjYfKpeccReo++NQ1/Vxo1o7Ws0WDdl8H6dFjJNDWPsj9nYvQ\nvXdEZDmwwzl3Y8brLzvnpvq917x3oqkdoq0/ytoh2vqjrB0qR7+f906Y3945FlgFTAV6RORs4Czn\n3FthzWkYhmH4E+YHuU8Cc31+PzWsuQ3DMIzcVMrlW8MwDKMEWNM3DMOIEdb0DcMwYoQ1fcMwjBhR\n6puzSsKLr3ay8o4N9Pb1U1NdxbLFxzBtUnPOnJ6+fmrz5IDOg+T2dc/ywIZtA/H82RNZNO+IrLEu\nXd3G257b7FsaYNUl6d4bWs+WL3yrjS6PK0FTHVz/5fSxftq2id+sH3TBOP34yXz0lJlZY112fRtv\nee6DO6AJVl5cnI+PxjtI62ei8aX59p1P8OQL7wzEc2QcSxfOzhorSJ+VIL2dNHXV1l6z7rVjadb9\nV29so33XYDxxHHzzc8X50miODdCtiaUr2uj2xPWj4DvLyu+9s+6PL/GT3740EC+adyjzZ2c/J/uu\nRzZz1++3DMRnnTyFM07IfuZusYzIM/1UM+8Hevr6WXnbhrw5+OSAzoPE2/AB7ntiW1YOkLaoAXLd\ncKz1bOnKsKHZlcNyxtvwAe75Q6YNUoK3MnTs2JWdo/W4CdI7SONL4234AI+7d7KTAiZIbydNXbW1\n16x77Viadd+esU62DaP0mmMDdGuiOyPeWyFmUt6GD3DH/S/lzPM2fICfPbwlZ16xjMimn2rm+WJt\nDkB75x7fOGhyebZEia49Pb5xXChHHbRrWkOp171ROkZk06+trvKNtTkArc1jfOOgyVSR97a6CqWx\nvjY9HlObJ3NkU446aNe0hlKve6N0jMimv2zxMdRWV1EFA9fr8+XgkwM6D5L5syf6xilaGvxj0Hu2\nNNX5x5C4hu8XpzigyT8GvcdNkN5BGl+aOTLONw6DIL2dNHXV1l6z7rVjadb9xHH+cSFojg3QrYn6\nUf5xuVg071DfOMVZJ0/xjYdL6N47w8G8d6KpHaKtP8raIdr6o6wdKke/n/dOhfwNNAzDMEqBNX3D\nMIwYYU3fMAwjRljTNwzDiBHW9A3DMGJEqDYMInIkcBdwnXPuRhGZAtwK1AI9wGLn3NYwNRiGYRiD\nhPnkrEbgBuABz8tXAzc75/6fiHwe+DKwLOi5Nf41Ws8WjQ/GFd9pY6vnFvTJzXD1Z4vz57j5Fxt4\nbFPHQHzCES188sPZ37cutW+IdixN7cuhK8ixNN4uWp8VzZyfX9nGHo+VQEMN3HhZti6Nf412GzXH\nR9T3Y6WOpfU0KpYwL+90A6cBXsOXzwH/lfy5HRgfxsQa/xqtZ4vGB2Nrxltf71RLzcLb8AEefbYj\nT2ZlovUOijIabxetz4qGPRnj7+7Nnaf1r9FQDk8jI0GQnka5CPNxib1Ar4h4X+sCEJFq4PPAv/qN\n0dLSQE1NdcFz5/KvaW0dO+T7NDnavLiOZbW3sWys8oylpeTWysmGvwZoc8494JfbUeSpShXpzacK\nVHfJae+ks7Hy51jtbSwbqzxjefH7I1GOb+/cCmx2zl0V1gQa/xqtZ4vGB2Nys39cCCcc0eIbVzpa\n76Aoo/F20fqsaGio8Y9TaP1rNJTD08hIEKSnUS5C994RkeXAjuS3d84DTnXOfVLzXvPeiaZ2iLb+\nKGuHaOuPsnaoHP1+3jthfnvnWGAVMBXoEZGzgQnAXhF5MJn2Z+fc58LSYBiGYaQT5ge5TwJzwxrf\nMAzDKBy7I9cwDCNGWNM3DMOIEdb0DcMwYoQ1fcMwjBhR8puzSsFDG7bww3WbB+ILTpvOSe9N/379\n+mff4Ht3PzcQL114OHNkUlFjXX3r7/jLtn0D8WGT6rji/BOzxtL46mh1/bRtE79ZP+hwcfrxk/no\nKTPTcrSeLavXrufplwfv/Z41rYlLPnZcWo7GUwdg1+59rLn3eTq79tHcWMeSBTNoGpP+HFatB8mK\nHz3K868PegvMPLieZYtPSMsJ0uNGq+v2dc/ywIZtA/H82RNZNO+ItBztftT4rLz4aicr79hAT1//\nwLNvp03KvhnkW7c/xp+3DN7QeOQhDXx50fvScrT10sz5jZse5LWOwQU2ZfworvrU3KyxND4+Gu2g\nq5dmPYNufX3hW210eWwvmurg+i9nrwnN8ag9hrT7qFhG5Jm+t0kD3PrrzVk53gMS4Ls/fy4rRzuW\nt+EDvPDGvqwc0PnqaHV5FxjAPX94PStH69niPUAAnnpxV1aO1lNnzb3P8/im7Wze0snjm7azZt3z\nuSdV4D0gATa9ujcrJ0iPGy3ehg9w3xPbsnK0+1Hjs5JqvgA9ff2svG1DzrG8TRPgmVey72jX1ksz\np7fhA2x5M4cJETofH4120NVLs55Bt766Mo6ZXbkPbdXxqD2Gwl7TI7LpG8GTy1MnF+2de3xjo3BS\nzTdfPFLmHOloj6GwsaZvqMi8vS/f7X6tzWN8Y6NwaqurfOORMudIR3sMhc2IbPoXnDbdN4bENVa/\nuJCxDptU5xun0PjqaHWdfvxk3xj0ni2zpjX5xqD31FmyYAZzZk5g+pRm5sycwJIFM3JPqmDmwfW+\nMQTrcaNl/uyJvjHo96PGZ2XZ4mMGmm7q+noujjykwTcGfb00c04ZP8o3TqHx8dFoB129NOsZdOur\nqc4/TqE5HrXHUNhrOnTvneFg3jvR1A7R1h9l7RBt/VHWDpWj3897Z0Se6RuGYRi5saZvGIYRI6zp\nG4ZhxAhr+oZhGDHCmr5hGEaMCNWGQUSOBO4Crks+OWsKiefjVgNvAEucc91hajAMwzAGUTV9EfkQ\nMN45d5uI3A4cB3zVOfczn/c0AjcA3oef/yvwbefcT0Xk34ELge8WrT4Py295mL/uGLx/euqEGq68\n8OS0nEtXt/G2567rlgZYdUm2p4bGe0frQaLxdrn1V0/zyDM7BuJTjj6A8z/03qz3aebUeslc8Z02\ntnpuZ5/cDFd/tjhdGn8hrS5NXpC11+rSeMlo66WZUzOfdqylK9rwnmXVj4LvLCtuG7XeTpdd38Zb\nHleFA5pg5cXF1V6zVjX+PNo5tbo0/lva/aj1ISoW7eWdK4H/Tjb/auAY4JIh3tMNnAZ4TSjmAr9M\n/nw3ME+ttAC8DR/g5e3ZpjNvZ9hsdOS2+lB572g9SDR4GwXAQ3/akTMvyDm3ZviXvN5ZvC6Nv1CQ\nBFkHLRovGW29gppPS+Y/q/fmKZdmTq2301sZx9aO3FY4KjRrVePPEzQa/y3tftT6EBWL9vLObufc\nDhE5HVjjnNslIn1+b3DO9QK9IuJ9udFzOWc7kG076KGlpYGammqlRH9aW8cGkmNj2Vg2lo1ViWNp\n0Tb9ehG5HPggcJmITAfeNcy5h7Se6Mh3+l0EmrvktHfS2Vg2lo1lY1XaWF78/khoL+98GjgIuMA5\ntxdYAHytIBUJdolIyoHrINIv/QTG1Ak1vjEkruH7xSk03jtaDxINpxx9gG8cxpyTm/3jQnRp/IWC\nJMg6aNF4yWjrFdR8WupH+ceFzKn1djqgyT8uBM1a1fjzBI3Gf0u7H7U+RMXi670jIn/j92bn3F+G\nmkBElgM7kt/euRl4OPmB8PXA0865W/K917x3oqkdoq0/ytoh2vqjrB0qR7+f985Ql3ce8PldP5D3\nj4KIHAusAqYCPSJyNnAe8AMR+QzwCvDDIeY3DMMwAsS36Tvnivb0dM49SeLbOpnML3ZMwzAMY3j4\nNn0R+ZHf751z/xisHMMwDCNMhnt5xzAMw4gQQ13eyXnNXUTqgNsB338JGIZhGJWF1oZhCXAt8O7k\nS/vx/1eAYRiGUYFob866BDgKWAucTuJbOG+HJWq4aPxy1j/7Bt+7+7mBeOnCw5kj2TcIb3yhndV3\nbqSfwedaHjm1NS0nSF8ajXaA29c9ywMbtg3E82dPZNG8I4raRs2cu3bvY829z9PeuYfW5jEsWTCD\npjHZ30XW1EvrZ6LxUNLWSzOn1vNEU1etLo1/jXY/XrSiLe2a6yjgliJ9fDT7cfXa9Tz98qDnwaxp\nTVzyseOyxlr3x5f4yW9fGogXzTuU+bPTvyOi2ddaXZpjA3T7W7tWNftbUwfQH2vFor2T5W3n3Fag\n2jnX5Zy7mYRZWkWi8cvxHkQA3/35c1k5wMACg8SHGNet3ZiVE6QvjUY7kLaoAe57YltWjnYbNXOu\nufd5Ht+0nZe37uTxTdtZs+75nGNp6qVF46GkrZcGreeJpq5aXRr/Gu1+zPyQLZetjtb/RbMfvQ0f\n4KkXc5vqeBsdwB33v5SVo9nXWl2aYwOC9bjR7G9NHUB/rBWL9ky/T0TOALYkb7Z6FjgkUCUVSuaB\nFNdPr9s79/jGKaxeI4NK3Y+VqitItMdasWjP9JcArwJfAiYDi4GLA1VSoWTe1jakYdAIpbV5jG+c\nwuo1MqjU/VipuoJEe6wVi7bpn+uce8o5t90592nn3JnASYEqCRCNX87ShYf7xikuPeeogYWVuoaY\nSZC+NBrtkLhO6ReDfhs1cy5ZMIM5Mycw9cCxzJk5gSULZuQcS1MvLRoPJW29NGg9TzR11erS+Ndo\n92PmwZzr4Nb6v2j246xpTb5xikXzDvWNQbevtbo0xwYE63Gj2d+aOoD+WCuWobx3TgU+QOLMfo3n\nV7UkzNcODFRNBua9E03tEG39UdYO0dYfZe1QOfqH472ziUHPe69/fg9wzjB1GYZhGCVmqJuz3gB+\nLCKPOudeBhCR0cAE59yWEugzDMMwAkT77Z1FIrILuAV4EtgpIvc6574RnjTDMAwjaLQf5H4YuBH4\nOHC3c+5vgfeHpsowDMMIBW3T73HO9QMfAn6RfC2Yh9cahmEYJUN7eadTRO4BDnbO/SF5o1auG/58\nEZEmEiZtLcBo4Crn3LpCxzEMwzCKQ9v0zyXx8JPfJ+Nu4Pwi5vsE4JxzXxeRyUAbMLOIcXzReOEE\n6XHzxWvb2LlvMB5XD6u/lO3PofHx0Pr4aOZcuqKNbk9cPwq+syxbl8bbResH8uKrnay8YwO9ff3U\nVFexbPExTJuU/iBTrZ+JJk/rZ6IZa8WPHuX51/cOxDMPrmfZ4hOy3pfaxp6+fmrzbKPWl0aj6+pb\nf8dftg3u7MMm1XHF+ScWNZZ2TWjWoXY/ajxutNuoOR6DrJd2GzW+R1pdGn+h4aC9vNNH4o7nM0Tk\nQmAKMK+I+XYA45M/tyTjwNF44QTpceNtvgDv7M1KUaP18dHM2Z0R783zbzONt4vWDyTVDPuBnr5+\nVt62IfekAaH1M9HgbfgAm17NvSNT2wj5t1HrS6PB2ygAXnhjX57ModGuCe061KDxuNFuo+Z4DLJe\nWjS+R1pdQfpX5UJ7pr+ORON/xfNaP/D9QiZzzq0VkU+IyAskmv7pfvktLQ3U1ATz0UFr69hAcuI6\nVmfXvqw411i9ff1ZcVS2UZsTh220sco3Vi5/Ie2cGrRNv9Y5d8pwJxORxcBfnXMfFJGjgf8Esn1d\nk3R0FO96l4nmLjntnXRxHKu5sS4rzjVWTXXVwFlwKo7KNmpz4rCNNlb5xqoivfFXFTBnCr8/EtrL\nO8+KyPih04bk/ST+1YBz7k/AZBEJ/FtAGi+cID1uxtX7x4Wg9fHRzFk/yj9OofF20fqBLFt8DLXV\nVVTBwPXuMNH6mWiYeXC9b5witY2Qfxu1vjQaDptU5xsXgnZNaNehBo3HjXYbNcdjkPXSovE90uoK\n0r8qF77eOylE5DfA+4DngAGja+dc9lMO/Mf5CjDRObdMRA4B7nPO5XUTMu+daGqHaOuPsnaItv4o\na4fK0T8c750UKwLSchPwfRF5KDn3ZwMa1zAMw1Dg2/RFJPWvlEeCmMw5t4vEXb2GYRhGGRjqTL+X\n3A+nSX3WYHflGoZhRIihXDa1H/QahmEYEcCaumEYRoywpm8YhhEjtN/eiRQa/5etb3Zxzdqn6NrT\nQ2N9LZefN4sDWxrzjuXns6LxFgGdH4vGBwd0Ph43/2IDj23qGIhPOKKFT3443O/Np+q6e28PDaNz\n11XrZ/LVG9to97gXTBwH3/xcep7WE0hTL23tNWg9gS5d3cbbHreHlgZYdUl4/kJaTyBNXbXrXlPX\nb9/5BE++8M5APEfGsXRh9n2bmrG0/lV3PbKZu34/+Cyos06ewhknpN+vo12rmrGCrP1wGJFn+hr/\nl2vWPkXHzm729e6nY1c31/z4Kd+x8BlL4y0COj8WjQ8O6Hw8vA0f4NFnO7JygiZV1+4e/7pqaM8o\nz7Z3snO0nkCaemlrr0HrCfR2hr1PrpvQg/QX0noCaeqqXfeaunobPsDjLsfOVo6l9Q3yNmmAnz1c\n/MMANWMFWfvhMCKbfk+GN0pmDNC1p8c3LmQsYxBtXYOivXOPb2wUh9W1fIRd+xHZ9FO3yOeLARrr\na9PjMbVZOdqxjEG0dQ2K1uYxvrFRHFbX8hF27Udk09f4v1x+3ixaxo6mrmYULWNHc/m5s3zHwmcs\njbcI6PxYND44oPPxOOGIFt84DFJ1HV3rX1cNE8f5x6D3BNLUS1t7DVpPoJYG/7iQsTRoPYE0ddWu\ne01d58g437iQsbS+QWedPMU3LgTNWEHWfjiovHfKhXnvRFM7RFt/lLVDtPVHWTtUjn4/750ReaZv\nGIZh5MaavmEYRoywpm8YhhEjrOkbhmHECGv6hmEYMaLkNgwich6wjIRt85XOuXtKrcEwDCOulLTp\nJ5+z+y/AsUATcBUQeNPXeO9ovDJA54PxhW+10dU7GDfVwfVfzvbn0Ph4pObr7NpHc2NdXt8Nja/O\n7eue5YEN2wbi+bMnsmjeEVljaX2INDy0YQs/XLd5IL7gtOmc9N707yxr/Uw0eVrtmrGW3/Iwf90x\nuCOnTqjhyguznwiqmVO7vjS6tB5KQW6jZt1ftKIt7WEbo4BbcuxHjUePdqyNL7Sz+s6N9DP4/Ngj\np7am5Wg9br5x04O81rF/IJ4yfhRXfWpuWo52rWq8nTTHBow87515wP3OuZ3OuTecc58OYxKN947W\nd0Pjg+Ft+AC7sm1d1KTm27yl09d3Q+Or4234APc9sS0rB/Q+RBq8ixrg1l9vzpMZDEFq9zZDgJe3\n9+bM08wZpK9LkB5K2m3UrPuIYN6OAAATYUlEQVTMm2j2Z2Uk0Hj0aMdKNfzUe65buzErR+tx4234\nAFvezDfr0Gi8nbTHRtjeO6W+vDMVaBCRXwItwHLn3AP5kltaGqipKfzhXL0Z/ji9ff20to4d8n25\ncjq79mXFxY6lySt2Pu2cuXJ27+3JirVzhqlLkzcc7aWuV9i6ghyr1Otem5P5x6F/GGMFqSvIsYbT\nAzSUuulXAeOBhcAhwG9F5BDnXM47bztyWQ4qqKmuSjNGq6muUt0llyunubEuKy52LE1esfNp58yV\n0zC6lu6e7sG4vjbQuwrDrNdwtJe6XmHrCnKsUq97bU7qOa3euBJ0BTnWcHpACr8/EqW+vLMNeNQ5\n1+ucexHYCbQO8Z6C0XjvaH03ND4YTXX+cSGk5ps+pdnXd0PjqzN/9kTfOIXWh0jDBadN942DJkjt\nUyfU+MaFzBmkr0uQHkrabdSs+8zmka+ZaDx6tGNdes5RpPwFUtf0M9F63EwZP8o3LgSNt5P22BhR\n3jsichDwA2ABics7/wMc6pzLeTHNvHeiqR2irT/K2iHa+qOsHSpHf8V47zjnXgPuBB4DfgN8IV/D\nNwzDMIKn5N/Td87dBNxU6nkNwzAMuyPXMAwjVljTNwzDiBHW9A3DMGKENX3DMIwYUfIPciuFlD9P\nT1//wHf5M/15gh7r23c+wZMvvDMQz5FxLF04u6g5NT4eWv+XIAnSe2fdH1/iJ799aSBeNO9Q5s9O\nfz6s1qdEo0vj6xI0Wn8kDRqPmyDX/U/bNvGb9a8PxKcfP5mPnjIzK2/9s2/wvbufG4iXLjycOTIp\nLUezr0G3j7TbqMn7/Mo29ni+X9hQAzdeVpwnkNYnaqR571QMqZ0N+f15gh7L2/ABHnfv5MzToPHx\nCNL/RUuQ3jveJgBwx/0vZeVofUo0ujS+LkGj9UfSoPG4CXLdexs+wD1/eD1nnrfhA3z3589l5Wj2\nNej2kXYbNXl7Mr5Qvju3VZFKl9YnKmzvndg2/Z4Mf57MuFxjGYXR3rnHNy6EXL4uI42or1XNPtJu\nY5C10Ojq2tPjG6cIck3nIrZNv7a6yjcu11hGYbQ2j/GNCyFzr43EvRj1tarZR9ptDLIWGl2N9bXp\n8ZjaHFnBrulcxLbpp/x5IL8/T9BjzZFxvnEhaHw8gvR/0RKk986ieYf6xqD3KdHo0vi6BI3WH0mD\nxuMmyHV/+vGTfeMUSxce7huDbl+Dbh9pt1GT11DjHxeiS+sTNaK8dwrFvHeiqR2irT/K2iHa+qOs\nHSpHf8V47xiGYRjlxZq+YRhGjLCmbxiGESOs6RuGYcQIa/qGYRgxoixNX0TGiMiLIvKJcsxvGIYR\nV8rlvfPPwFthDZ7yrujs2kdzY11O7wqtP4fGL0PrlfHFa9vY6XnQ/bh6WP2ldB8PjXaA1WvX8/TL\nuwbiWdOauORjx6Xl3Pqrp3nkmR0D8SlHH8D5H3pvjooFh8aDJEjvHa2fiaZeQfrgaLniO21s9bhx\nTG6Gqz+bXguNdw3AZ1a04b3Hsw74XkZdtWtCs6a/emMb7YMlZeI4+ObnsvejxvdoxY8e5fnX9w7E\nMw+uZ9niE7LG0tRC6wmkybvs+jbe8rhZHNAEKy/O3sZUP+nt66cmTz/RrtWwKfmZvojMBN4D3BPW\nHCnvis1bOvN6V2j9OTR+GVqvDG/DB3hnb3aORjuQ1sAAnnpxV1aO9+AGeOhPO7JygiZI/xqNH4vW\nz0RTryB9cLRszbBfer0zO0fjXQOQeVP/vhw52jWhWdPtGSXclsdKSuN75G34AJtezXFwoKuF1hNI\nk/dWhn3RjuxlAwz2k37y9xPtWg2bcpzprwIuBs4fKrGlpYGamuqCJ+js2pcVt7aOTXutN8Nno7ev\nPysHYPfenqw4M08zXz7CHKvYnOGQy4MkSF2ZeZr9M5w5w65XsXOGvY3FrsNy1L4SxtL0k+Gs1SAp\nadMXkX8E/uCce0lEhszv6Mh2CdTQ3FiXFWfeJVdTXZVmsFRTXZXzTrqG0bV093QPxvW1WXma+fIR\n5ljF5gyHKtIbf5VyzmK3UbN/hjNnOe6uDLNe2pxi12E5al8JY2n6yXDWaqH4/TEp9eWd04EzReQx\n4JPAN0RkXtCTpLwrpk9pzutdofXn0PhlaL0yxtX7x1rtkLgm7RdD4nqtXxwGQfrXaPxYtH4mmnoF\n6YOjZXKzfww67xpIXMP3i0G/JjRreuI4/ziFxvdo5sH1vnEKTS20nkCavAOa/OMUqX5SRf5+ol2r\nYVM27x0RWQ687Jz7Qb4c896JpnaItv4oa4do64+ydqgc/ea9YxiGYQBlfFyic255ueY2DMOIK3am\nbxiGESOs6RuGYcQIa/qGYRgxwpq+YRhGjLCmbxiGESPK9u2dkYTWcE1r8qahUsybikFjfgY68zZt\n7TVGXZr5giZIQ78g66VBY6SmRWs0WMhYQ22jJk9rdhcl7Ew/ALSGa1qTNw2VYt5UDBrzM9CZt2lr\nrzHqCtIsTkuQhn5B1kuDxkhNi9ZosJCxhtpGTZ7W7C5KWNMPgPbOPb5xip4MU6bMuBC69vT4xiOB\nXOZtmWhrH9R8QaPZj9ptLHW9giRIXdqxKrUWYWNNPwBam8f4xilSXj/54kJorK9Nj8fU5smMLpnV\nyVUtbe2Dmi9oNPtRu42lrleQBKlLO1al1iJsqpcvX15uDXnZvXvf8uG8v7FxNLt353IVD5bDD2lm\nx9t7qasZxfSDm1myYAZ1tdmW0O/5mxYee2Yr+/sHTZnePTa3sdRQ2o+ePp7/eX4H+/f3M66xjsvP\nnVX0NdAw8NP/yhvtbO0Y/N2saU387REHZeVNO7iJx57ZDgxeo57QnH69W1v7ya31PLFp0Dt+6cLD\nOeiAdCdCzXxBo9mP2m0Msl4a3j2uhqc2Dz4L6YLTpnPIxHcVNVZKV+OYWqZNHjcsXdpt1ORp1o2X\nUvWcoWhsHH1Vvt+VzXBNgxmuRVM7RFt/lLVDtPVHWTtUjn4zXDMMwzAAa/qGYRixwpq+YRhGjLCm\nbxiGESNKfkeuiKwETkrO/U3n3M9KrcEwDCOulPRMX0ROBY50zh0PfBBYXcr5DcMw4k6pz/QfBtYn\nf+4EGkWk2jnXV2IdZSFIrxKNj0+QPitaNB4q37jpQV7r2D8QTxk/iqs+NTdUXZrap3xwdu/toWF0\nafyMgvTeCcMLx29OrZeUJi+V09vXT43PWBp/Ia0vlXnvlADnXJ9zrisZXgT8Oi4NH4L1KtH4+ATp\ns6JF46HibfgAW97cn5UTNJrap3xwuntK52cUpPdOGF44fnNqvaQ0eamc/iHG0vgLaX2p4uq9UxaX\nTRE5k0TT/3u/vJaWBmpqirsrL0Vra/675yoBP31+v+vN8O3p7evPyu/s2pcVh12PYucsx37KnHP3\n3p6sOGxdmjmHsx+L1a+ZU7MGtXnasXL5CxW7H8Naq5Xec8rxQe4C4J+ADzrn3vbL7ejYPay5KuXu\nOD/y6RtKe011VZphW011VVZ+c2NdVhx2PYqdsxz7KXPOhtG1dPd0D8b1taHr0sw5nP1YrH7NnJo1\nqM3TjlVFeuOvovj9GMZarZSe4/eHp6TeOyLyLuAOEg1/x1D5UfHe0VKIV8lQ2jU+PkH6rGjReKj8\nz3Ov8M6ewUN3yvhRnHrs1FB1aWqf8sHp7y+dn1GQ3jtheOH4zan1ktLkpXL6hxhL4y+k9aUy750S\nICKfBpYD3otn/+ic+2uufPPeiaZ2iLb+KGuHaOuPsnaoHP1+3jslvbzjnLsZuLmUcxqGYRiD2B25\nhmEYMcKavmEYRoywpm8YhhEjrOkbhmHECGv6hmEYMaIsd+SONLTeKFpPECN4yuFDVGq0/jUjHe2+\njsOayIWd6QeA1htF6wliBE85fIhKjda/ZqSj3ddxWBO5sKYfAO2de3zjFF17enxjIzy0+yjK9GT4\n12TGcUG7r+OwJnJhTT8AWpvH+MYpGutr0+MxtTnzjODR7qMoU1td5RvHBe2+jsOayIVd0w+AJQtm\nAKRdG8zF5efN4pofJ6/pj6nl8nNnlVJmrNHuoyizbPExrLwt/Zp+HNHu6zisiVyU1HunUMx7J5ra\nIdr6o6wdoq0/ytqhcvT7ee/Y5R3DMIwYYU3fMAwjRljTNwzDiBHW9A3DMGKENX3DMIwYUY5n5F4H\nvI/Eoy6/6Jx7vNQaDMMw4kpJm76InAJMd84dLyKHA98Hji+lBiOexMH3KOUl09m1j+bGuth4yRiF\nUerLO38H/ALAOfcc0CIi40qswYghcfA9SnnJbN7SGSsvGaMwSn1550DgSU/cnnztnVzJfjcYaGlt\nzf/k+konytqhsvR37OzeBTR64q7W1rFN+fIrSbuWxzdtXw/M8cSPX9k69rgySiqKKNbeS6XrL7cN\nQzzNQYySc/eqM/M2+JHC3avOjFyDN0pPqS/vvE7izD7FZOCNEmswDMOILaVu+vcCZwOIyP8CXnfO\nld+owjAMIyaU3HBNRFYAJwP7gc875/5UUgGGYRgxpqJdNg3DMIxgsTtyDcMwYoQ1fcMwjBhR7q9s\nhkKUrR5EZC7wU+DZ5EsbnXNfKJ8iHSJyJHAXcJ1z7kYRmQKsAapJfENriXOuu5wa85FD+w+AY4E3\nkynXOOfuKZe+oRCRlcBJJI7nbwKPE53aZ2r/CBGpvYg0AD8AJgL1wL8Bf6LCaz/izvS9Vg/ARcD1\nZZZUDA855+Ym/4tCw28EbgAe8Lz8r8C3nXMnAS8AF5ZD21Dk0Q7wdc8+qMimAyAipwJHJtf7B4HV\nRKf2ubRDRGoPfBh4wjl3CvBx4FoiUPsR1/Qxq4dy0A2cRuI+jBRzgV8mf74bmFdiTVpyaY8SDwMf\nS/7cSeKu47lEo/a5tFeXT05hOOd+4pxbmQynAK8SgdqPxMs7BVk9VCjvEZFfAu8GrnLO3VduQX44\n53qBXhHxvtzo+WftdmBSyYUpyKMd4GIR+TIJ7Rc753aUXJwC51wf0JUMLwJ+DSyISO1zae8jIrVP\nISKPAgcDZwD3V3rtR+KZfiZRs3rYDFwFnAmcD/yniETdKjFq+2AN8DXn3AeAp4Dl5ZUzNCJyJonG\neXHGryq+9hnaI1d759wJJD6LuI30eldk7Udi04+01YNz7rXkPxv7nXMvAluBg8qtqwh2iciY5M8H\nEaHLJ865B5xzKRvOXwJHlVPPUIjIAuCfgA85594mQrXP1B6l2ovIsckvLJDUXAPsrPTaj8SmH2mr\nBxE5T0QuS/58IIlvBrxWXlVFcT/w0eTPHwX+u4xaCkJE/ktE/iYZzgWeKaMcX0TkXcA1wBnOubeS\nL0ei9rm0R6n2JJwFvgIgIhOBJiJQ+xF5R26UrR5EZCzwY6AZqCNxTf/X5VXlj4gcC6wCpgI9JP5I\nnUfi62z1wCvABc65njJJzEse7TcAXwN2A7tIaN9eLo1+iMinSVwC8Zrnnw/cQuXXPpf2W0lc5olC\n7ccA/0niQ9wxJC7LPgH8iAqu/Yhs+oZhGEZuRuLlHcMwDCMP1vQNwzBihDV9wzCMGGFN3zAMI0ZY\n0zcMw4gRI9GGwYgZIjKJxPe9jwJS92Qsd87d7/Oexc6520qhT4OIzAIu8jPYE5HJwEznXFvplBkj\nDTvTNyKNiFSRMNj7g3PuaOfcicBS4DYRmZbnPdXAlSWUOSTOuacUjqqnAh8ohR5j5GLf0zcijYjM\nA652zr0v4/UWYB+JG2XeDYwFfuqc+z8i8kPgHBIW1n8vIh8HvkDCK6Ud+KRz7k0RuRD4UvK1R4B5\nzrkTRWQG8D0SJ001JLxifpf04e8GBPgtcKhz7hNJPf8AfNQ59/E82zE3uR0nisiDJO7sPAGYAfwL\n8GhyzCrgP5xz1w6vckZcsTN9I+ocQeKhIWk45zqACcAvnHOnAu8HrkjabP8L0J5s+FNIeL/MS/4r\n4UFP3jXAfOfc35FoviluAL7rnJtL4l8VP/L8rjH5+irg70WkKfn6x0ncJaulyTl3GgkjsmXOuZdI\n3OG8xhq+MRys6RtRp4/8HuzbgZOS1rfrSNwa/+6MnONJ2N+uS55hn5OMZwCvOOe2JfP+y/OevwXu\nA3DObQTGicgByd89mnx9F4mncZ2dbPzvIXH2ruXB5P9fyaHZMIrGPsg1os5G4JOZL4rIUSTsbkcD\n73fO9YtILl/2bmC9c+6MjPcfR8K7KUWf5+fMa6JVntf2eV6/icQZfzew1jm3Hz29GeMbRiDYmb4R\naZxzD5Gws/1a6jUROYKELe+JwJ+TDf8jQAOJPwL7gdpk+uPAcUlHU0TkY0l/9xeBacnPBgAWeqZ9\nDFiQzD8GeNM59yYZJO12x5AwELs1gM316jaMorAzfWMkcDpwrYg8Q+KB2nuBfyBx1n1H0rP9LuD2\n5H/vA7aKyJMk3Fi/CPxKRHaTcHc8P/lB7v8Gfi8ir5B4Gtshyfm+AHxPRD5Logkv8dF2G/AR59xf\nA9jOR4CfiMg+59w3AhjPiCH27R3DyIOILAHucc69lXx8nzjnPlPA+6tI/IvjBufcvWHpNIxCsDN9\nw8hPE9AmIm+T8Nq/QPvG5AN8bgHWpRq+iBwPfDPPW85xzm0dpl7DGBI70zcMw4gR9kGuYRhGjLCm\nbxiGESOs6RuGYcQIa/qGYRgxwpq+YRhGjPj/507k9NkPMMkAAAAASUVORK5CYII=\n",
            "text/plain": [
              "<matplotlib.figure.Figure at 0x7feccf331588>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "metadata": {
        "id": "6wIVlruf435B",
        "colab_type": "code",
        "outputId": "f7f0f76a-407e-4cbd-98a2-0b53a0a53fb4",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 350
        }
      },
      "cell_type": "code",
      "source": [
        "data = pd.concat([df['Installs'],df['Rating']], axis=1)\n",
        "fig = sns.boxplot(x='Rating', y=\"Installs\", data=data)\n",
        "fig.axis(ymin=0, ymax=18);"
      ],
      "execution_count": 119,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/seaborn/categorical.py:454: FutureWarning:\n",
            "\n",
            "remove_na is deprecated and is a private function. Do not use.\n",
            "\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<matplotlib.figure.Figure at 0x7feccf4fd0f0>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "metadata": {
        "id": "LZEeRQiqgenI",
        "colab_type": "code",
        "outputId": "57b994d6-638d-4cc4-881e-635ee3371d5e",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "from sklearn.linear_model import LinearRegression\n",
        "\n",
        "feature_col =['Reviews','Size','Type','Rating','Price','Content Rating','Genres','Category_int']\n",
        "x=df[feature_col]\n",
        "y=df.Installs\n",
        "print(x.shape,y.shape)"
      ],
      "execution_count": 108,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "(9360, 8) (9360,)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "rjf4J5RQkpLU",
        "colab_type": "code",
        "outputId": "e984b361-0647-470f-95f7-e0a304c810f8",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 84
        }
      },
      "cell_type": "code",
      "source": [
        "from sklearn.preprocessing import MinMaxScaler\n",
        "x_c = x[:]\n",
        "x_trans = MinMaxScaler().fit_transform(x_c)"
      ],
      "execution_count": 109,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/sklearn/preprocessing/data.py:323: DataConversionWarning:\n",
            "\n",
            "Data with input dtype int64, float64 were all converted to float64 by MinMaxScaler.\n",
            "\n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "metadata": {
        "id": "n83TPf-2pAdE",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "x_train,x_test,y_train,y_test = train_test_split(x_trans,y,test_size = 0.3)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "RohayYvZqZeP",
        "colab_type": "code",
        "outputId": "0b9122e2-9476-4e0e-8750-7801e65131d9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "print(x_train.shape,y_train.shape)"
      ],
      "execution_count": 111,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "(6552, 8) (6552,)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "JMKej5sqLv5s",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "lm = LinearRegression()\n",
        "m = lm.fit(x_train,y_train)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "wjY4eaI6MXoR",
        "colab_type": "code",
        "outputId": "e253b1e8-659c-4e77-e818-8466b98ecac5",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        }
      },
      "cell_type": "code",
      "source": [
        "m.score(x_test,y_test)\n",
        "print ('R^2 is: \\n', m.score(x_test,y_test))"
      ],
      "execution_count": 113,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "R^2 is: \n",
            " 0.2230400921703688\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "It3Ic91XPTgo",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}