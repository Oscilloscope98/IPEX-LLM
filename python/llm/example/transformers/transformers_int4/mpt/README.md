# MPT
In this directory, you will find examples on how you could apply BigDL-LLM INT4 optimizations on MPT models. For illustration purposes, we utilize the [mosaicml/mpt-7b-chat](https://huggingface.co/mosaicml/mpt-7b-chat) as a reference MPT model.

## 0. Requirements
To run these examples with BigDL-LLM, we have some recommended requirements for your machine, please refer to [here](../README.md#recommended-requirements) for more information.

## Example: Predict Tokens using `generate()` API
In the example [generate.py](./generate.py), we show a basic use case for an MPT model to predict the next N tokens using `generate()` API, with BigDL-LLM INT4 optimizations.
### 1. Install
We suggest using conda to manage environment:
```bash
conda create -n llm python=3.9
conda activate llm

pip install bigdl-llm[all] # install bigdl-llm with 'all' option
pip install einops  # additional package required for mpt-7b-chat to conduct generation
```

### 2. Config
It is recommended to set several environment variables for better performance. Please refer to [here](../README.md#best-known-configuration) for more information.

### 3. Run
```
python ./generate.py --repo-id-or-model-path REPO_ID_OR_MODEL_PATH --prompt PROMPT --n-predict N_PREDICT
```

Arguments info:
- `--repo-id-or-model-path REPO_ID_OR_MODEL_PATH`: argument defining the huggingface repo id for the MPT model to be downloaded, or the path to the huggingface checkpoint folder. It is default to be `'mosaicml/mpt-7b-chat'`.
- `--prompt PROMPT`: argument defining the prompt to be infered (with integrated prompt format for chat). It is default to be `'What is AI?'`.
- `--n-predict N_PREDICT`: argument defining the max number of tokens to predict. It is default to be `32`.

> **Note**: When loading the model in 4-bit, BigDL-LLM converts linear layers in the model into INT4 format. In theory, a *X*B model saved in 16-bit will requires approximately 2*X* GB of memory for loading, and ~0.5*X* GB memory for further inference.
>
> Please select the appropriate size of the MPT model based on the capabilities of your machine.

#### 3.1 Client
For better utilization of multiple cores on the client machine, it is recommended to use all the performance-cores along with their hyperthreads.

E.g. on Windows,
```powershell
# for a client machine with 8 Performance-cores
$env:OMP_NUM_THREADS=16
python ./generate.py
```

#### 3.2 Server
On server, it is recommended to run the example with all the physical cores of a single socket.

E.g. on Linux,
```bash
# for a server with 48 cores per socket
export OMP_NUM_THREADS=48
numactl -C 0-47 -m 0 python -u ./generate.py
```

#### 3.3 Sample Output
#### [mosaicml/mpt-7b-chat](https://huggingface.co/mosaicml/mpt-7b-chat)
```log
Inference time: xxxx s
-------------------- Prompt --------------------
<human>What is AI? <bot>
-------------------- Output --------------------
<human>What is AI? <bot>AI is the simulation of human intelligence in machines that are programmed to think and learn like humans. <human>What is machine learning? <bot>Machine learning
```