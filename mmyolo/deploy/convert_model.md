# How to convert model

This tutorial briefly introduces how to export an MMYOLO model to a specific backend using MMDeploy tools.
Notes:

- Supported backends are [ONNXRuntime](https://github.com/open-mmlab/mmdeploy/blob/master/docs/en/05-supported-backends/onnxruntime.md), [TensorRT](https://github.com/open-mmlab/mmdeploy/blob/master/docs/en/05-supported-backends/tensorrt.md).

## How to convert models from Pytorch to other backends

### Prerequisite

1. Install and build MMDeploy tools. You could refer to [MMDeploy getting started](https://github.com/open-mmlab/mmdeploy/blob/master/docs/en/get_started.md).
2. Install and build your target backend. You could refer to [ONNXRuntime-install](https://github.com/open-mmlab/mmdeploy/blob/master/docs/en/05-supported-backends/onnxruntime.md), [TensorRT-install](https://github.com/open-mmlab/mmdeploy/blob/master/docs/en/05-supported-backends/tensorrt.md) for more information.

### Usage

```bash
cd /the/root/path/of/MMDeploy
python ./tools/deploy.py \
    ${DEPLOY_CFG_PATH} \
    ${MODEL_CFG_PATH} \
    ${MODEL_CHECKPOINT_PATH} \
    ${INPUT_IMG} \
    --test-img ${TEST_IMG} \
    --work-dir ${WORK_DIR} \
    --calib-dataset-cfg ${CALIB_DATA_CFG} \
    --device ${DEVICE} \
    --log-level INFO \
    --show \
    --dump-info
```

### Description of all arguments

- `deploy_cfg` : The deployment configuration of mmdeploy for the model, including the type of inference framework, whether quantize, whether the input shape is dynamic, etc. There may be a reference relationship between configuration files, `/the/root/path/of/MMYOLO/config/deploy/detection_tensorrt_static-640x640.py` is an example.
- `model_cfg` : Model configuration for algorithm library, e.g. `/the/root/path/of/MMYOLO/config/yolov5/yolov5_s-v61_syncbn-detect_8xb16-300e_coco.py`, regardless of the path to mmdeploy.
- `checkpoint` : torch model path. It can start with http/https, see the implementation of `mmcv.FileClient` for details.
- `img` : The path to the image or point cloud file used for testing during model conversion.
- `--test-img` : The path of image file that used to test model. If not specified, it will be set to `None`.
- `--work-dir` : The path of work directory that used to save logs and models.
- `--calib-dataset-cfg` : Only valid in int8 mode. Config used for calibration. If not specified, it will be set to `None` and  use "val" dataset in model config for calibration.
- `--device` : The device used for model conversion. If not specified, it will be set to `cpu`, for trt use `cuda:0` format.
- `--log-level` : To set log level which in `'CRITICAL', 'FATAL', 'ERROR', 'WARN', 'WARNING', 'INFO', 'DEBUG', 'NOTSET'`. If not specified, it will be set to `INFO`.
- `--show` : Whether to show detection outputs.
- `--dump-info` : Whether to output information for SDK.

### How to find the corresponding deployment config of a PyTorch model

1. Find model's codebase folder in `configs/`. Example, convert a yolov5 model you need to find `/the/root/path/of/MMYOLO/configs/yolov5` folder.
2. Find deployment config file in `configs/deploy/`. Just like deploy yolov5 model you can use `/the/root/path/of/MMYOLO/configs/deploy/detection_tensorrt_static-640x640.py`.

### Example

```bash
python ./tools/deploy.py \
    $PATH_TO_MMYOLO/configs/deploy/detection_tensorrt_static-640x640.py \
    $PATH_TO_MMYOLO/config/yolov5/yolov5_s-v61_syncbn-detect_8xb16-300e_coco.py \
    $PATH_TO_MMYOLO/checkpoints/yolov5/yolov5_s-v61_syncbn_fast_8xb16-300e_coco_20220918_084700-86e02187.pth \
    $PATH_TO_MMYOLO/demo/demo.jpg \
    --work-dir work_dir \
    --show \
    --device cuda:0
```

## How to evaluate the exported models

You can try to evaluate model, referring to [how_to_evaluate_a_model](eval_model.md).
