{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "WebAppIrisDataSet.py",
      "provenance": [],
      "authorship_tag": "ABX9TyNXIYz149grjdNz4VLOaU38",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Aleena-Mishra-10/Web-App/blob/master/WebAppIrisDataSet_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bpRKKhOtXr8c",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "outputId": "ff1d3e22-dd69-40bb-fe31-0b4ff4536c4c"
      },
      "source": [
        "#!pip install streamlit\n"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Collecting streamlit\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/b0/c5/963a1d9ebf5916d836652e94390846bffb4258c478d75bf01852a5fe79fa/streamlit-0.61.0-py2.py3-none-any.whl (7.1MB)\n",
            "\u001b[K     |████████████████████████████████| 7.1MB 2.7MB/s \n",
            "\u001b[?25hRequirement already satisfied: packaging in /usr/local/lib/python3.6/dist-packages (from streamlit) (20.4)\n",
            "Requirement already satisfied: altair>=3.2.0 in /usr/local/lib/python3.6/dist-packages (from streamlit) (4.1.0)\n",
            "Requirement already satisfied: click>=7.0 in /usr/local/lib/python3.6/dist-packages (from streamlit) (7.1.2)\n",
            "Collecting toml\n",
            "  Downloading https://files.pythonhosted.org/packages/9f/e1/1b40b80f2e1663a6b9f497123c11d7d988c0919abbf3c3f2688e448c5363/toml-0.10.1-py2.py3-none-any.whl\n",
            "Collecting pydeck>=0.1.dev5\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/80/43/ac1282dc135dd3c2cfabe13257e97401f688a1e9771c58c7a9a57bcc63ba/pydeck-0.4.0b2-py2.py3-none-any.whl (4.4MB)\n",
            "\u001b[K     |████████████████████████████████| 4.4MB 17.3MB/s \n",
            "\u001b[?25hCollecting watchdog\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/73/c3/ed6d992006837e011baca89476a4bbffb0a91602432f73bd4473816c76e2/watchdog-0.10.2.tar.gz (95kB)\n",
            "\u001b[K     |████████████████████████████████| 102kB 10.7MB/s \n",
            "\u001b[?25hCollecting validators\n",
            "  Downloading https://files.pythonhosted.org/packages/c4/4a/4f9c892f9a9f08ee5f99c32bbd4297499099c2c5f7eff8c617a57d31a7d8/validators-0.15.0.tar.gz\n",
            "Requirement already satisfied: tzlocal in /usr/local/lib/python3.6/dist-packages (from streamlit) (1.5.1)\n",
            "Requirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.6/dist-packages (from streamlit) (7.0.0)\n",
            "Collecting base58\n",
            "  Downloading https://files.pythonhosted.org/packages/3c/03/58572025c77b9e6027155b272a1b96298e711cd4f95c24967f7137ab0c4b/base58-2.0.1-py3-none-any.whl\n",
            "Requirement already satisfied: boto3 in /usr/local/lib/python3.6/dist-packages (from streamlit) (1.14.2)\n",
            "Requirement already satisfied: botocore>=1.13.44 in /usr/local/lib/python3.6/dist-packages (from streamlit) (1.17.2)\n",
            "Requirement already satisfied: cachetools>=4.0 in /usr/local/lib/python3.6/dist-packages (from streamlit) (4.1.0)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.6/dist-packages (from streamlit) (1.18.5)\n",
            "Requirement already satisfied: protobuf>=3.6.0 in /usr/local/lib/python3.6/dist-packages (from streamlit) (3.10.0)\n",
            "Requirement already satisfied: pandas>=0.21.0 in /usr/local/lib/python3.6/dist-packages (from streamlit) (1.0.4)\n",
            "Collecting tornado<6.0,>=5.0\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/e6/78/6e7b5af12c12bdf38ca9bfe863fcaf53dc10430a312d0324e76c1e5ca426/tornado-5.1.1.tar.gz (516kB)\n",
            "\u001b[K     |████████████████████████████████| 522kB 41.1MB/s \n",
            "\u001b[?25hRequirement already satisfied: requests in /usr/local/lib/python3.6/dist-packages (from streamlit) (2.23.0)\n",
            "Requirement already satisfied: astor in /usr/local/lib/python3.6/dist-packages (from streamlit) (0.8.1)\n",
            "Collecting blinker\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/1b/51/e2a9f3b757eb802f61dc1f2b09c8c99f6eb01cf06416c0671253536517b6/blinker-1.4.tar.gz (111kB)\n",
            "\u001b[K     |████████████████████████████████| 112kB 40.4MB/s \n",
            "\u001b[?25hCollecting enum-compat\n",
            "  Downloading https://files.pythonhosted.org/packages/55/ae/467bc4509246283bb59746e21a1a2f5a8aecbef56b1fa6eaca78cd438c8b/enum_compat-0.0.3-py3-none-any.whl\n",
            "Requirement already satisfied: python-dateutil in /usr/local/lib/python3.6/dist-packages (from streamlit) (2.8.1)\n",
            "Requirement already satisfied: pyparsing>=2.0.2 in /usr/local/lib/python3.6/dist-packages (from packaging->streamlit) (2.4.7)\n",
            "Requirement already satisfied: six in /usr/local/lib/python3.6/dist-packages (from packaging->streamlit) (1.12.0)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.6/dist-packages (from altair>=3.2.0->streamlit) (2.11.2)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.6/dist-packages (from altair>=3.2.0->streamlit) (0.3)\n",
            "Requirement already satisfied: jsonschema in /usr/local/lib/python3.6/dist-packages (from altair>=3.2.0->streamlit) (2.6.0)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.6/dist-packages (from altair>=3.2.0->streamlit) (0.10.0)\n",
            "Collecting ipykernel>=5.1.2; python_version >= \"3.4\"\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/61/18/f2350f0396fca562c22f880e25d668eaf6de129b6a56bf5b6786796a12e1/ipykernel-5.3.0-py3-none-any.whl (119kB)\n",
            "\u001b[K     |████████████████████████████████| 122kB 45.3MB/s \n",
            "\u001b[?25hRequirement already satisfied: traitlets>=4.3.2 in /usr/local/lib/python3.6/dist-packages (from pydeck>=0.1.dev5->streamlit) (4.3.3)\n",
            "Requirement already satisfied: ipywidgets>=7.0.0 in /usr/local/lib/python3.6/dist-packages (from pydeck>=0.1.dev5->streamlit) (7.5.1)\n",
            "Collecting pathtools>=0.1.1\n",
            "  Downloading https://files.pythonhosted.org/packages/e7/7f/470d6fcdf23f9f3518f6b0b76be9df16dcc8630ad409947f8be2eb0ed13a/pathtools-0.1.2.tar.gz\n",
            "Requirement already satisfied: decorator>=3.4.0 in /usr/local/lib/python3.6/dist-packages (from validators->streamlit) (4.4.2)\n",
            "Requirement already satisfied: pytz in /usr/local/lib/python3.6/dist-packages (from tzlocal->streamlit) (2018.9)\n",
            "Requirement already satisfied: s3transfer<0.4.0,>=0.3.0 in /usr/local/lib/python3.6/dist-packages (from boto3->streamlit) (0.3.3)\n",
            "Requirement already satisfied: jmespath<1.0.0,>=0.7.1 in /usr/local/lib/python3.6/dist-packages (from boto3->streamlit) (0.10.0)\n",
            "Requirement already satisfied: urllib3<1.26,>=1.20; python_version != \"3.4\" in /usr/local/lib/python3.6/dist-packages (from botocore>=1.13.44->streamlit) (1.24.3)\n",
            "Requirement already satisfied: docutils<0.16,>=0.10 in /usr/local/lib/python3.6/dist-packages (from botocore>=1.13.44->streamlit) (0.15.2)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.6/dist-packages (from protobuf>=3.6.0->streamlit) (47.3.1)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.6/dist-packages (from requests->streamlit) (3.0.4)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.6/dist-packages (from requests->streamlit) (2020.4.5.2)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.6/dist-packages (from requests->streamlit) (2.9)\n",
            "Requirement already satisfied: MarkupSafe>=0.23 in /usr/local/lib/python3.6/dist-packages (from jinja2->altair>=3.2.0->streamlit) (1.1.1)\n",
            "Requirement already satisfied: jupyter-client in /usr/local/lib/python3.6/dist-packages (from ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (5.3.4)\n",
            "Requirement already satisfied: ipython>=5.0.0 in /usr/local/lib/python3.6/dist-packages (from ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (5.5.0)\n",
            "Requirement already satisfied: ipython-genutils in /usr/local/lib/python3.6/dist-packages (from traitlets>=4.3.2->pydeck>=0.1.dev5->streamlit) (0.2.0)\n",
            "Requirement already satisfied: nbformat>=4.2.0 in /usr/local/lib/python3.6/dist-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (5.0.7)\n",
            "Requirement already satisfied: widgetsnbextension~=3.5.0 in /usr/local/lib/python3.6/dist-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (3.5.1)\n",
            "Requirement already satisfied: pyzmq>=13 in /usr/local/lib/python3.6/dist-packages (from jupyter-client->ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (19.0.1)\n",
            "Requirement already satisfied: jupyter-core>=4.6.0 in /usr/local/lib/python3.6/dist-packages (from jupyter-client->ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (4.6.3)\n",
            "Requirement already satisfied: prompt-toolkit<2.0.0,>=1.0.4 in /usr/local/lib/python3.6/dist-packages (from ipython>=5.0.0->ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (1.0.18)\n",
            "Requirement already satisfied: pexpect; sys_platform != \"win32\" in /usr/local/lib/python3.6/dist-packages (from ipython>=5.0.0->ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (4.8.0)\n",
            "Requirement already satisfied: pickleshare in /usr/local/lib/python3.6/dist-packages (from ipython>=5.0.0->ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (0.7.5)\n",
            "Requirement already satisfied: pygments in /usr/local/lib/python3.6/dist-packages (from ipython>=5.0.0->ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (2.1.3)\n",
            "Requirement already satisfied: simplegeneric>0.8 in /usr/local/lib/python3.6/dist-packages (from ipython>=5.0.0->ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (0.8.1)\n",
            "Requirement already satisfied: notebook>=4.4.1 in /usr/local/lib/python3.6/dist-packages (from widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (5.2.2)\n",
            "Requirement already satisfied: wcwidth in /usr/local/lib/python3.6/dist-packages (from prompt-toolkit<2.0.0,>=1.0.4->ipython>=5.0.0->ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (0.2.4)\n",
            "Requirement already satisfied: ptyprocess>=0.5 in /usr/local/lib/python3.6/dist-packages (from pexpect; sys_platform != \"win32\"->ipython>=5.0.0->ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (0.6.0)\n",
            "Requirement already satisfied: nbconvert in /usr/local/lib/python3.6/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (5.6.1)\n",
            "Requirement already satisfied: terminado>=0.3.3; sys_platform != \"win32\" in /usr/local/lib/python3.6/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.8.3)\n",
            "Requirement already satisfied: defusedxml in /usr/local/lib/python3.6/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.6.0)\n",
            "Requirement already satisfied: mistune<2,>=0.8.1 in /usr/local/lib/python3.6/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.8.4)\n",
            "Requirement already satisfied: testpath in /usr/local/lib/python3.6/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.4.4)\n",
            "Requirement already satisfied: bleach in /usr/local/lib/python3.6/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (3.1.5)\n",
            "Requirement already satisfied: pandocfilters>=1.4.1 in /usr/local/lib/python3.6/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.4.2)\n",
            "Requirement already satisfied: webencodings in /usr/local/lib/python3.6/dist-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.1)\n",
            "Building wheels for collected packages: watchdog, validators, tornado, blinker, pathtools\n",
            "  Building wheel for watchdog (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for watchdog: filename=watchdog-0.10.2-cp36-none-any.whl size=73605 sha256=915cba6e45a9cf53dc6bc8a7cf0dbeb6f4551df8f17f0f45a70b93106b268dd6\n",
            "  Stored in directory: /root/.cache/pip/wheels/bc/ed/6c/028dea90d31b359cd2a7c8b0da4db80e41d24a59614154072e\n",
            "  Building wheel for validators (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for validators: filename=validators-0.15.0-cp36-none-any.whl size=18371 sha256=8f701fee472a3ad95e74f43d6708db5e4768c1f7422eba14442855d77ecc55ac\n",
            "  Stored in directory: /root/.cache/pip/wheels/56/48/64/66c29f8eaf756b780549db047057e1563dfd2d2ce8e3d316c1\n",
            "  Building wheel for tornado (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for tornado: filename=tornado-5.1.1-cp36-cp36m-linux_x86_64.whl size=462329 sha256=ae9a999550d0f9c7d922372ae5039a64f3f282c6a0d589b4df03e1a4dd4dd9d6\n",
            "  Stored in directory: /root/.cache/pip/wheels/6d/e1/ce/f4ee2fa420cc6b940123c64992b81047816d0a9fad6b879325\n",
            "  Building wheel for blinker (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for blinker: filename=blinker-1.4-cp36-none-any.whl size=13449 sha256=9ccba8dc1d292a2aa9999c830ae4a76ae5038e04c251d58ce0703d3c8695c2b1\n",
            "  Stored in directory: /root/.cache/pip/wheels/92/a0/00/8690a57883956a301d91cf4ec999cc0b258b01e3f548f86e89\n",
            "  Building wheel for pathtools (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pathtools: filename=pathtools-0.1.2-cp36-none-any.whl size=8784 sha256=ce4e3968131ccab355a2be628f9a5f5dcde044031bb735766a418cacd0f4ebba\n",
            "  Stored in directory: /root/.cache/pip/wheels/0b/04/79/c3b0c3a0266a3cb4376da31e5bfe8bba0c489246968a68e843\n",
            "Successfully built watchdog validators tornado blinker pathtools\n",
            "\u001b[31mERROR: google-colab 1.0.0 has requirement ipykernel~=4.10, but you'll have ipykernel 5.3.0 which is incompatible.\u001b[0m\n",
            "Installing collected packages: toml, tornado, ipykernel, pydeck, pathtools, watchdog, validators, base58, blinker, enum-compat, streamlit\n",
            "  Found existing installation: tornado 4.5.3\n",
            "    Uninstalling tornado-4.5.3:\n",
            "      Successfully uninstalled tornado-4.5.3\n",
            "  Found existing installation: ipykernel 4.10.1\n",
            "    Uninstalling ipykernel-4.10.1:\n",
            "      Successfully uninstalled ipykernel-4.10.1\n",
            "Successfully installed base58-2.0.1 blinker-1.4 enum-compat-0.0.3 ipykernel-5.3.0 pathtools-0.1.2 pydeck-0.4.0b2 streamlit-0.61.0 toml-0.10.1 tornado-5.1.1 validators-0.15.0 watchdog-0.10.2\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.colab-display-data+json": {
              "pip_warning": {
                "packages": [
                  "ipykernel",
                  "tornado"
                ]
              }
            }
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HhSOor61W2lx",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "from sklearn import datasets\n",
        "from sklearn.ensemble import RandomForestClassifier"
      ],
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qAA7Bp8pXIvA",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "st.write(\"\"\"\n",
        "#Sample iris prediction app\n",
        "This app predicts the **iris flower** type !!\n",
        "\"\"\")"
      ],
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DC1VCGZYYxte",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "def user_input_features():\n",
        "    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)\n",
        "    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)\n",
        "    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)\n",
        "    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)\n",
        "    data = {'sepal_length': sepal_length,\n",
        "            'sepal_width': sepal_width,\n",
        "            'petal_length': petal_length,\n",
        "            'petal_width': petal_width}\n",
        "    features = pd.DataFrame(data, index=[0])\n",
        "    return features"
      ],
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "X_ErCxsNaFG4",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "df = user_input_features()"
      ],
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YRW6X_qCadrY",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "st.subheader('User Input parameters')\n",
        "st.write(df)"
      ],
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "l7QsmZHkahyk",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "iris = datasets.load_iris()\n",
        "X = iris.data\n",
        "Y = iris.target"
      ],
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JLcwmBuralxR",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 156
        },
        "outputId": "c3672565-b3bd-47b9-9cb1-96c2be006701"
      },
      "source": [
        "clf = RandomForestClassifier()\n",
        "clf.fit(X, Y)"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "RandomForestClassifier(bootstrap=True, ccp_alpha=0.0, class_weight=None,\n",
              "                       criterion='gini', max_depth=None, max_features='auto',\n",
              "                       max_leaf_nodes=None, max_samples=None,\n",
              "                       min_impurity_decrease=0.0, min_impurity_split=None,\n",
              "                       min_samples_leaf=1, min_samples_split=2,\n",
              "                       min_weight_fraction_leaf=0.0, n_estimators=100,\n",
              "                       n_jobs=None, oob_score=False, random_state=None,\n",
              "                       verbose=0, warm_start=False)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gTaYCDbpap_7",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "prediction = clf.predict(df)\n",
        "prediction_proba = clf.predict_proba(df)"
      ],
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "C4QxZ4l8a2b8",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "st.subheader('Class labels and their corresponding index number')\n",
        "st.write(iris.target_names)"
      ],
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "TV07iMvbb1TS",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "st.subheader('Prediction')\n",
        "st.write(iris.target_names[prediction])\n",
        "#st.write(prediction)"
      ],
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XwYxvg7Ucpxo",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "st.subheader('Prediction Probability')\n",
        "st.write(prediction_proba)\n"
      ],
      "execution_count": 12,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "W9n_z2nLcr4m",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "\n"
      ],
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "LjMD_UrZc3C0",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}