#
# Copyright (c) 2025, Neptune Labs Sp. z o.o.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.project_alias_group_dto import ProjectAliasGroupDTO
    from ..models.report_node_dto import ReportNodeDTO
    from ..models.report_version_metadata_dto import ReportVersionMetadataDTO


T = TypeVar("T", bound="ReportVersionDTO")


@_attrs_define
class ReportVersionDTO:
    """
    Attributes:
        metadata (ReportVersionMetadataDTO):
        nodes (List['ReportNodeDTO']):
        report_name (str):
        experiment_aliases (Union[Unset, List['ProjectAliasGroupDTO']]): List of experiment aliases
        run_aliases (Union[Unset, List['ProjectAliasGroupDTO']]): List of run id aliases
    """

    metadata: "ReportVersionMetadataDTO"
    nodes: List["ReportNodeDTO"]
    report_name: str
    experiment_aliases: Union[Unset, List["ProjectAliasGroupDTO"]] = UNSET
    run_aliases: Union[Unset, List["ProjectAliasGroupDTO"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metadata = self.metadata.to_dict()

        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.to_dict()
            nodes.append(nodes_item)

        report_name = self.report_name

        experiment_aliases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.experiment_aliases, Unset):
            experiment_aliases = []
            for experiment_aliases_item_data in self.experiment_aliases:
                experiment_aliases_item = experiment_aliases_item_data.to_dict()
                experiment_aliases.append(experiment_aliases_item)

        run_aliases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.run_aliases, Unset):
            run_aliases = []
            for run_aliases_item_data in self.run_aliases:
                run_aliases_item = run_aliases_item_data.to_dict()
                run_aliases.append(run_aliases_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadata": metadata,
                "nodes": nodes,
                "reportName": report_name,
            }
        )
        if experiment_aliases is not UNSET:
            field_dict["experimentAliases"] = experiment_aliases
        if run_aliases is not UNSET:
            field_dict["runAliases"] = run_aliases

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_alias_group_dto import ProjectAliasGroupDTO
        from ..models.report_node_dto import ReportNodeDTO
        from ..models.report_version_metadata_dto import ReportVersionMetadataDTO

        d = src_dict.copy()
        metadata = ReportVersionMetadataDTO.from_dict(d.pop("metadata"))

        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = ReportNodeDTO.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        report_name = d.pop("reportName")

        experiment_aliases: Union[Unset, List[ProjectAliasGroupDTO]] = UNSET
        _experiment_aliases = d.pop("experimentAliases", UNSET)
        if not isinstance(_experiment_aliases, Unset):
            experiment_aliases = []
            for experiment_aliases_item_data in _experiment_aliases:
                experiment_aliases_item = ProjectAliasGroupDTO.from_dict(experiment_aliases_item_data)

                experiment_aliases.append(experiment_aliases_item)

        run_aliases: Union[Unset, List[ProjectAliasGroupDTO]] = UNSET
        _run_aliases = d.pop("runAliases", UNSET)
        if not isinstance(_run_aliases, Unset):
            run_aliases = []
            for run_aliases_item_data in _run_aliases:
                run_aliases_item = ProjectAliasGroupDTO.from_dict(run_aliases_item_data)

                run_aliases.append(run_aliases_item)

        report_version_dto = cls(
            metadata=metadata,
            nodes=nodes,
            report_name=report_name,
            experiment_aliases=experiment_aliases,
            run_aliases=run_aliases,
        )

        report_version_dto.additional_properties = d
        return report_version_dto

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
