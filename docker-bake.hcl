## buildx bake configurations ###
variable "TAG" {
    default = "" 
}

variable "COMPANY_NAME" { 
    default = "erguotou" 
}

variable "PREFIX_NAME" { 
    default = "docs"
} 

variable "PRODUCT_EDITION" {
    default = ""
}

variable "DOCKERFILE" {
    default = "Dockerfile"
}

variable "NOPLUG_POSTFIX" {
    default = ""
}

variable "DS_VERSION_HASH" {
    default = ""
}

variable "REGISTRY" {
    default = "docker.io"
}

variable "PRODUCT_BASEURL" {
    default = "https://download.onlyoffice.com/install/documentserver/linux/onlyoffice-documentserver"
}

variable "RELEASE_VERSION" {
    default = ""
}

group "apps" {
    targets = ["proxy", "converter", "docservice", "example"]
}

target "example" {
    target = "example"
    dockerfile = "${DOCKERFILE}"
    tags = equal("docker.io",REGISTRY) ? ["${REGISTRY}/${COMPANY_NAME}/${PREFIX_NAME}-example${PRODUCT_EDITION}:${TAG}"] : [
                                          "${REGISTRY}/${PREFIX_NAME}-example${PRODUCT_EDITION}:${TAG}" ]
    platforms = ["linux/amd64", "linux/arm64"]
    args = {
        "PRODUCT_EDITION": "${PRODUCT_EDITION}"
    }
}

target "proxy" {
    target = "proxy"
    dockerfile = "${DOCKERFILE}"
    tags = equal("docker.io",REGISTRY) ? ["${REGISTRY}/${COMPANY_NAME}/${PREFIX_NAME}-proxy${PRODUCT_EDITION}:${TAG}${NOPLUG_POSTFIX}"] : [
                                          "${REGISTRY}/${PREFIX_NAME}-proxy${PRODUCT_EDITION}:${TAG}${NOPLUG_POSTFIX}" ]
    platforms = ["linux/amd64", "linux/arm64"]
    args = {
        "PRODUCT_EDITION": "${PRODUCT_EDITION}"
        "DS_VERSION_HASH": "${DS_VERSION_HASH}"
        "PRODUCT_BASEURL": "${PRODUCT_BASEURL}"
        "RELEASE_VERSION": "${RELEASE_VERSION}"
    }
}

target "converter" {
    target = "converter"
    dockerfile = "${DOCKERFILE}"
    tags = equal("docker.io",REGISTRY) ? ["${REGISTRY}/${COMPANY_NAME}/${PREFIX_NAME}-converter${PRODUCT_EDITION}:${TAG}${NOPLUG_POSTFIX}"] : [
                                          "${REGISTRY}/${PREFIX_NAME}-converter${PRODUCT_EDITION}:${TAG}${NOPLUG_POSTFIX}" ]
    platforms = ["linux/amd64", "linux/arm64"]
    args = {
        "PRODUCT_EDITION": "${PRODUCT_EDITION}"
        "DS_VERSION_HASH": "${DS_VERSION_HASH}"
        "PRODUCT_BASEURL": "${PRODUCT_BASEURL}"
        "RELEASE_VERSION": "${RELEASE_VERSION}"
    }
}

target "docservice" {
    target = "docservice"
    dockerfile = "${DOCKERFILE}"
    tags = equal("docker.io",REGISTRY) ? ["${REGISTRY}/${COMPANY_NAME}/${PREFIX_NAME}-docservice${PRODUCT_EDITION}:${TAG}${NOPLUG_POSTFIX}"] : [
                                          "${REGISTRY}/${PREFIX_NAME}-docservice${PRODUCT_EDITION}:${TAG}${NOPLUG_POSTFIX}" ]
    platforms = ["linux/amd64", "linux/arm64"]
    args = {
        "PRODUCT_EDITION": "${PRODUCT_EDITION}"
        "DS_VERSION_HASH": "${DS_VERSION_HASH}"
        "PRODUCT_BASEURL": "${PRODUCT_BASEURL}"
        "RELEASE_VERSION": "${RELEASE_VERSION}"
    }
}

target "utils" {
    target = "utils"
    dockerfile = "${DOCKERFILE}"
    tags = equal("docker.io",REGISTRY) ? ["${REGISTRY}/${COMPANY_NAME}/${PREFIX_NAME}-utils:${TAG}"] : [
                                          "${REGISTRY}/${PREFIX_NAME}-utils:${TAG}" ]
    platforms = ["linux/amd64", "linux/arm64"]
    args = {
        "DS_VERSION_HASH": "${DS_VERSION_HASH}"
        "PRODUCT_BASEURL": "${PRODUCT_BASEURL}"
        "RELEASE_VERSION": "${RELEASE_VERSION}"
    }
}

target "balancer" {
    target = "balancer"
    dockerfile = "${DOCKERFILE}"
    tags = equal("docker.io",REGISTRY) ? ["${REGISTRY}/${COMPANY_NAME}/${PREFIX_NAME}-balancer:${TAG}"] : [
                                          "${REGISTRY}/${PREFIX_NAME}-balancer:${TAG}" ]
    platforms = ["linux/amd64", "linux/arm64"]
}

