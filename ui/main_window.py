from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QListWidget, QTextEdit, QGroupBox, QApplication
)
from data.project_info import PROJECT_NAME, PROJECT_SLOGAN, REPOSITORY_STATUS
from data.members import MEMBERS
from data.features import FEATURES
from data.progress import PROGRESS_ITEMS
from data.changelog import CHANGELOG


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("班级项目协作看板")
        self.setGeometry(100, 100, 900, 600)

        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)

        # 顶部：项目信息
        info_group = QGroupBox("项目信息")
        info_layout = QVBoxLayout()
        info_layout.addWidget(QLabel(f"<b>项目名称：</b>{PROJECT_NAME}"))
        info_layout.addWidget(QLabel(f"<b>项目口号：</b>{PROJECT_SLOGAN}"))
        info_layout.addWidget(QLabel(f"<b>仓库状态：</b>{REPOSITORY_STATUS}"))
        info_group.setLayout(info_layout)
        main_layout.addWidget(info_group)

        # 中间三列
        mid_layout = QHBoxLayout()

        # 左侧：成员卡片
        members_group = QGroupBox("小组成员")
        members_layout = QVBoxLayout()
        self.members_list = QListWidget()
        for m in MEMBERS:
            self.members_list.addItem(
                f"[{m['role']}] {m['name']}\n任务：{m['task']}"
            )
        members_layout.addWidget(self.members_list)
        members_group.setLayout(members_layout)
        mid_layout.addWidget(members_group)

        # 中间：功能清单
        features_group = QGroupBox("项目功能清单")
        features_layout = QVBoxLayout()
        self.features_list = QListWidget()
        for f in FEATURES:
            self.features_list.addItem(f"• {f}")
        features_layout.addWidget(self.features_list)
        features_group.setLayout(features_layout)
        mid_layout.addWidget(features_group)

        # 右侧：进度追踪
        progress_group = QGroupBox("Issue / PR 进度")
        progress_layout = QVBoxLayout()
        self.progress_list = QListWidget()
        for p in PROGRESS_ITEMS:
            self.progress_list.addItem(
                f"{p['issue']} | {p['owner']}\n{p['title']} - {p['status']}"
            )
        progress_layout.addWidget(self.progress_list)
        progress_group.setLayout(progress_layout)
        mid_layout.addWidget(progress_group)

        main_layout.addLayout(mid_layout)

        # 底部：版本日志
        changelog_group = QGroupBox("版本日志")
        changelog_layout = QVBoxLayout()
        self.changelog_edit = QTextEdit()
        self.changelog_edit.setPlainText("\n".join(CHANGELOG))
        self.changelog_edit.setReadOnly(True)
        changelog_layout.addWidget(self.changelog_edit)
        changelog_group.setLayout(changelog_layout)
        main_layout.addWidget(changelog_group)
