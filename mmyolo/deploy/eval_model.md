# How to evaluate model

After converting a PyTorch model to a backend model, you may evaluate backend models with `tools/test.py`

## Prerequisite

Install MMDeploy according to [get-started](https://github.com/open-mmlab/mmdeploy/blob/master/docs/en/get_started.md) instructions.
And convert the PyTorch model or ONNX model to the backend model by following the [guide](convert_model.md).

## Usage

```shell
python tools/test.py \
${DEPLOY_CFG} \
${MODEL_CFG} \
--model ${BACKEND_MODEL_FILES} \
[--out ${OUTPUT_PKL_FILE}] \
[--format-only] \
[--metrics ${METRICS}] \
[--show] \
[--show-dir ${OUTPUT_IMAGE_DIR}] \
[--show-score-thr ${SHOW_SCORE_THR}] \
--device ${DEVICE} \
[--cfg-options ${CFG_OPTIONS}] \
[--metric-options ${METRIC_OPTIONS}]
[--log2file work_dirs/output.txt]
[--batch-size ${BATCH_SIZE}]
[--speed-test] \
[--warmup ${WARM_UP}] \
[--log-interval ${LOG_INTERVERL}] \
```

## Description of all arguments

- `deploy_cfg`: The config for deployment.
- `model_cfg`: The config of the model in MMYOLO.
- `--model`: The backend model file. For example, if we convert a model to TensorRT, we need to pass the model file with ".engine" suffix.
- `--out`:  The path to save output results in pickle format. (The results will be saved only if this argument is given)
- `--format-only`: Whether format the output results without evaluation or not. It is useful when you want to format the result to a specific format and submit it to the test server
- `--metrics`: The metrics to evaluate the model defined in MMYOLO. e.g. "proposal" for COCO label.
- `--show`: Whether to show the evaluation result on the screen.
- `--show-dir`: The directory to save the evaluation result. (The results will be saved only if this argument is given)
- `--show-score-thr`: The threshold determining whether to show detection bounding boxes.
- `--device`: The device that the model runs on. Note that some backends restrict the device. For example, TensorRT must run on cuda.
- `--cfg-options`: Extra or overridden settings that will be merged into the current deploy config.
- `--metric-options`: Custom options for evaluation. The key-value pair in xxx=yyy
  format will be kwargs for dataset.evaluate() function.
- `--log2file`: log evaluation results (and speed) to file.
- `--batch-size`: the batch size for inference, which would override `samples_per_gpu` in data config. Default is `1`. Note that not all models support `batch_size>1`.
- `--speed-test`:  Whether to activate speed test.
- `--warmup`: warmup before counting inference elapse, require setting speed-test first.
- `--log-interval`: The interval between each log, require setting speed-test first.

\* Other arguments in `tools/test.py` are used for speed test. They have no concern with evaluation.

## Example

```shell
cd /the/root/path/of/MMDeploy
python tools/test.py \
    $PATH_TO_MMYOLO/configs/deploy/detection_tensorrt_static-640x640.py \
    $PATH_TO_MMYOLO/config/yolov5/yolov5_s-v61_syncbn-detect_8xb16-300e_coco.py \
    --model end2end.engine \
    --out out.pkl \
    --device cuda:0 \
    --speed-test
```
