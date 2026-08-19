#!/usr/bin/env bash

set -euo pipefail

APP_NAME="nexora-agent"
APP_USER="nexora-agent"
INSTALL_DIR="/opt/nexora-agent"
SERVICE_FILE="/etc/systemd/system/${APP_NAME}.service"

REPO_URL="https://github.com/kapusta123b/NexoraControl.git"
REPO_BRANCH="main"

echo "==> Installing ${APP_NAME}"

# --------------------------------------------------
# 1. Root
# --------------------------------------------------

if [[ "${EUID}" -ne 0 ]]; then
    echo "Run this installer with sudo."
    exit 1
fi

# --------------------------------------------------
# 2. Dependencies
# --------------------------------------------------

command -v git >/dev/null 2>&1 || {
    echo "git is required"
    exit 1
}

command -v python3 >/dev/null 2>&1 || {
    echo "python3 is required"
    exit 1
}

# --------------------------------------------------
# 3. Dedicated user
# --------------------------------------------------

if ! id "${APP_USER}" >/dev/null 2>&1; then
    useradd \
        --system \
        --home-dir "${INSTALL_DIR}" \
        --create-home \
        --shell /usr/sbin/nologin \
        "${APP_USER}"
fi

# --------------------------------------------------
# 4. Prepare directory
# --------------------------------------------------

mkdir -p "${INSTALL_DIR}"

TMP_DIR="$(mktemp -d)"

cleanup() {
    rm -rf "${TMP_DIR}"
}

trap cleanup EXIT

# --------------------------------------------------
# 5. Download only agent/
# --------------------------------------------------

echo "==> Downloading agent"

git clone \
    --depth 1 \
    --filter=blob:none \
    --sparse \
    --branch "${REPO_BRANCH}" \
    "${REPO_URL}" \
    "${TMP_DIR}/repo"

cd "${TMP_DIR}/repo"

git sparse-checkout set agent

# --------------------------------------------------
# 6. Copy agent contents
# --------------------------------------------------

echo "==> Installing agent files"

cp -a agent/. "${INSTALL_DIR}/"

# --------------------------------------------------
# 7. Python venv
# --------------------------------------------------

echo "==> Creating virtual environment"

python3 -m venv "${INSTALL_DIR}/.venv"

# --------------------------------------------------
# 8. Dependencies
# --------------------------------------------------

echo "==> Installing Python dependencies"

"${INSTALL_DIR}/.venv/bin/pip" install \
    --upgrade pip

"${INSTALL_DIR}/.venv/bin/pip" install \
    -r "${INSTALL_DIR}/requirements.txt"

# --------------------------------------------------
# 9. Permissions
# --------------------------------------------------

echo "==> Configuring permissions"

chown -R "${APP_USER}:${APP_USER}" "${INSTALL_DIR}"

# --------------------------------------------------
# 10. systemd
# --------------------------------------------------

echo "==> Installing systemd service"

cat > "${SERVICE_FILE}" <<EOF
[Unit]
Description=NexoraControl Agent
After=network-online.target
Wants=network-online.target

[Service]
Type=simple

User=${APP_USER}
Group=${APP_USER}

WorkingDirectory=${INSTALL_DIR}

ExecStart=${INSTALL_DIR}/.venv/bin/python ${INSTALL_DIR}/main.py

Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload

systemctl enable "${APP_NAME}"

# --------------------------------------------------
# 11. Initial setup
# --------------------------------------------------

echo
echo "==> Starting NexoraControl setup"
echo

sudo -u "${APP_USER}" \
    "${INSTALL_DIR}/.venv/bin/python" \
    "${INSTALL_DIR}/main.py setup"

# --------------------------------------------------
# 12. Start service
# --------------------------------------------------

echo
echo "==> Starting systemd service"

systemctl start "${APP_NAME}"

echo
echo "==> Installation completed"
echo

systemctl status "${APP_NAME}" --no-pager